"""
scientific.registry
===================

The *mathematical model registry*: the single place where a model is described
with its full provenance, and where the four representation layers are kept
apart on purpose.

Why four layers?
----------------
A model that is used for teaching must be able to answer four different
questions, and each question needs a different representation:

    source   "What does the book actually say?"      -> verbatim expression
    symbolic "What does it mean, and is it correct?" -> SymPy expression
    numeric  "How is it evaluated?"                  -> NumPy / SciPy code
    render   "How is it shown to the learner?"       -> MathML

The layers are linked by an id, never merged.  A symbolic expression may only
replace a source expression after an automated equivalence check has passed;
the result of that check is stored in the registry so a reader can see *that*
the conversion was verified, not just that it happened.

Data classes
------------
``SourceEquation``     the formula as recorded in the book / workspace registry
``SymbolicExpression`` the SymPy form plus the assumptions it was built under
``MathMLFormula``      the render layer
``EquationSpec``       one equation with all layers and its provenance
``ModelSpec``          one model: equations, parameters, assumptions, method,
                       execution entry points, reference cases, numerical limits
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Callable, Iterable

# --------------------------------------------------------------------------
# verification vocabulary — the same wording the rest of the workspace uses
# --------------------------------------------------------------------------

STATUS_BOOK_VERIFIED = "BOOK_EVIDENCE_VERIFIED"
STATUS_SYMBOLIC_VERIFIED = "SYMBOLIC_EQUIVALENCE_VERIFIED"
STATUS_NUMERIC_VERIFIED = "NUMERIC_REFERENCE_VERIFIED"
STATUS_UNVERIFIED = "FORMULA_UNVERIFIED"

#: Data-origin labels.  These are the only labels allowed in artifacts, and
#: they are intentionally different from each other so that a reader can never
#: confuse a book number with a simulated one.
ORIGIN_BOOK = "book"                 # value/equation taken from the book
ORIGIN_DERIVED = "derived"           # computed from a verified formula
ORIGIN_SOLVER = "solver"             # produced by a numerical solver
ORIGIN_ILLUSTRATIVE = "illustrative"  # made up for teaching
ORIGIN_UNVERIFIED = "unverified"     # formula/model not verified yet


class RegistryError(ValueError):
    """Raised when a registry entry is structurally invalid."""


# --------------------------------------------------------------------------
# layers
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class SourceEquation:
    """The formula exactly as the source records it.

    ``expression`` is the verbatim string taken from the workspace equation
    registry (e.g. ``k̇ = s f(k) - (n+g+δ)k``).  It is never edited, only
    quoted.

    ``pages_verified`` is the page the formula was actually *found* on, read
    back from the extracted pages.  It is filled in by the build, not typed
    in by hand, and it may differ from ``pages`` — when it does, the two are
    both kept so the discrepancy stays visible.
    """

    expression: str
    equation_ids: list[str] = field(default_factory=list)
    pages: str = ""
    section: str = ""
    catalog_status: str = STATUS_BOOK_VERIFIED
    equation_tag: str = ""
    pages_verified: str = ""
    provenance_status: str = ""

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SymbolicExpression:
    """The SymPy form of an equation, with the assumptions it relies on.

    ``expression`` is SymPy source code, e.g. ``"s * k**alpha - (n + g + delta) * k"``.
    ``assumptions`` are the SymPy symbol assumptions that make the expression
    well defined (``positive=True`` and friends).

    ``equivalence`` records the outcome of the automated check that ties this
    layer back to the source layer.  It stays ``None`` until the check has
    actually run.
    """

    expression: str
    assumptions: dict[str, dict[str, bool]] = field(default_factory=dict)
    equivalence: dict[str, Any] | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class MathMLFormula:
    """The render layer: MathML that a browser can display offline."""

    mathml: str
    text_fallback: str = ""
    display: bool = True

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EquationSpec:
    """One equation, described through all four layers."""

    id: str
    title_vi: str
    title_en: str = ""
    source: SourceEquation | None = None
    symbolic: SymbolicExpression | None = None
    render: MathMLFormula | None = None
    variables: list[dict[str, str]] = field(default_factory=list)
    parameters: list[dict[str, str]] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    valid_domain: dict[str, Any] = field(default_factory=dict)
    numerical_method: str = ""
    method_note_vi: str = ""
    plain_language_vi: str = ""
    verification_status: str = STATUS_UNVERIFIED

    def as_dict(self) -> dict[str, Any]:
        out = {
            "id": self.id,
            "title_vi": self.title_vi,
            "title_en": self.title_en,
            "variables": self.variables,
            "parameters": self.parameters,
            "assumptions": self.assumptions,
            "valid_domain": self.valid_domain,
            "numerical_method": self.numerical_method,
            "method_note_vi": self.method_note_vi,
            "plain_language_vi": self.plain_language_vi,
            "verification_status": self.verification_status,
        }
        if self.source:
            out["source"] = self.source.as_dict()
        if self.symbolic:
            out["symbolic"] = self.symbolic.as_dict()
        if self.render:
            out["render"] = self.render.as_dict()
        return out


@dataclass
class ReferenceCase:
    """A test case with a result that was verified by hand or in the book."""

    name: str
    description_vi: str = ""
    params: dict[str, float] = field(default_factory=dict)
    expected: dict[str, float] = field(default_factory=dict)
    tolerance: float = 1e-9
    source: str = ""
    origin: str = ORIGIN_BOOK

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ModelSpec:
    """A model with its provenance, its layers, and how to run it."""

    model_id: str
    name_vi: str
    name_en: str = ""
    chapter_id: str = ""
    book_source: dict[str, Any] = field(default_factory=dict)
    equations: list[EquationSpec] = field(default_factory=list)
    parameters: list[dict[str, Any]] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    valid_domain: dict[str, Any] = field(default_factory=dict)
    numerical_method: str = ""
    execution: dict[str, str] = field(default_factory=dict)
    reference_cases: list[ReferenceCase] = field(default_factory=list)
    numerical_limits: dict[str, Any] = field(default_factory=dict)
    verification_status: str = STATUS_UNVERIFIED
    notes_vi: str = ""

    # -- lookups ------------------------------------------------------------
    def equation(self, eq_id: str) -> EquationSpec:
        for eq in self.equations:
            if eq.id == eq_id:
                return eq
        raise RegistryError(f"{self.model_id}: không có phương trình '{eq_id}'")

    def validate(self) -> list[str]:
        """Structural checks.  Returns a list of problems (empty = valid)."""
        problems: list[str] = []
        if not self.model_id:
            problems.append("model_id rỗng")
        if not self.equations:
            problems.append(f"{self.model_id}: chưa có phương trình nào")
        for eq in self.equations:
            if eq.source is None and eq.symbolic is None:
                problems.append(f"{eq.id}: cả lớp nguồn và lớp ký hiệu đều trống")
            if eq.source is None and eq.render is not None:
                problems.append(
                    f"{eq.id}: có lớp render nhưng thiếu lớp nguồn — không được hiển thị "
                    "công thức chưa truy ngược được về sách"
                )
            if eq.symbolic is not None and eq.symbolic.equivalence is None:
                problems.append(
                    f"{eq.id}: lớp ký hiệu chưa có kết quả kiểm tra tương đương"
                )
            if eq.render is not None and not eq.render.mathml.strip():
                problems.append(f"{eq.id}: lớp render rỗng")
        if not self.execution:
            problems.append(f"{self.model_id}: chưa khai báo cách thực thi")
        return problems

    def as_dict(self) -> dict[str, Any]:
        return {
            "model_id": self.model_id,
            "name_vi": self.name_vi,
            "name_en": self.name_en,
            "chapter_id": self.chapter_id,
            "book_source": self.book_source,
            "equations": [e.as_dict() for e in self.equations],
            "parameters": self.parameters,
            "assumptions": self.assumptions,
            "valid_domain": self.valid_domain,
            "numerical_method": self.numerical_method,
            "execution": self.execution,
            "reference_cases": [c.as_dict() for c in self.reference_cases],
            "numerical_limits": self.numerical_limits,
            "verification_status": self.verification_status,
            "notes_vi": self.notes_vi,
        }


# --------------------------------------------------------------------------
# registry container
# --------------------------------------------------------------------------


class ModelRegistry:
    """An ordered collection of :class:`ModelSpec`."""

    def __init__(self, models: Iterable[ModelSpec] | None = None) -> None:
        self._models: list[ModelSpec] = list(models or [])

    def add(self, model: ModelSpec) -> ModelSpec:
        problems = model.validate()
        if problems:
            raise RegistryError("; ".join(problems))
        self._models.append(model)
        return model

    def get(self, model_id: str) -> ModelSpec:
        for m in self._models:
            if m.model_id == model_id:
                return m
        raise RegistryError(f"không có mô hình '{model_id}'")

    def models(self) -> list[ModelSpec]:
        return list(self._models)

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "generator": "scientific.registry",
            "models": [m.as_dict() for m in self._models],
        }

    def save(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.as_dict(), ensure_ascii=False, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        return path

    @classmethod
    def load(cls, path: Path) -> "ModelRegistry":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        models = []
        for m in raw.get("models", []):
            equations = []
            for e in m.get("equations", []):
                src = e.get("source")
                sym = e.get("symbolic")
                ren = e.get("render")
                equations.append(
                    EquationSpec(
                        id=e["id"],
                        title_vi=e.get("title_vi", ""),
                        title_en=e.get("title_en", ""),
                        source=SourceEquation(
                            **{
                                k: v
                                for k, v in (src or {}).items()
                                if k in SourceEquation.__dataclass_fields__
                            }
                        ) if src else None,
                        symbolic=SymbolicExpression(**sym) if sym else None,
                        render=MathMLFormula(**ren) if ren else None,
                        variables=e.get("variables", []),
                        parameters=e.get("parameters", []),
                        assumptions=e.get("assumptions", []),
                        valid_domain=e.get("valid_domain", {}),
                        numerical_method=e.get("numerical_method", ""),
                        method_note_vi=e.get("method_note_vi", ""),
                        plain_language_vi=e.get("plain_language_vi", ""),
                        verification_status=e.get("verification_status", STATUS_UNVERIFIED),
                    )
                )
            models.append(
                ModelSpec(
                    model_id=m["model_id"],
                    name_vi=m.get("name_vi", ""),
                    name_en=m.get("name_en", ""),
                    chapter_id=m.get("chapter_id", ""),
                    book_source=m.get("book_source", {}),
                    equations=equations,
                    parameters=m.get("parameters", []),
                    assumptions=m.get("assumptions", []),
                    valid_domain=m.get("valid_domain", {}),
                    numerical_method=m.get("numerical_method", ""),
                    execution=m.get("execution", {}),
                    reference_cases=[ReferenceCase(**c) for c in m.get("reference_cases", [])],
                    numerical_limits=m.get("numerical_limits", {}),
                    verification_status=m.get("verification_status", STATUS_UNVERIFIED),
                    notes_vi=m.get("notes_vi", ""),
                )
            )
        return cls(models)


# --------------------------------------------------------------------------
# convenience: build a SymPy expression from a spec
# --------------------------------------------------------------------------


def symbolic_namespace(expr: SymbolicExpression) -> dict[str, Any]:
    """Turn a :class:`SymbolicExpression` into a SymPy namespace.

    Symbols are created with the recorded assumptions, so an expression such as
    ``k**(alpha - 1)`` is only built with ``k > 0`` and ``alpha > 0`` where the
    registry says so.
    """
    from sympy import Symbol

    ns: dict[str, Any] = {}
    for name, assumptions in expr.assumptions.items():
        ns[name] = Symbol(name, **assumptions)
    return ns
