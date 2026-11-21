import fitz, json
from pathlib import Path

pdfs = {
  "HAN": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\econometrics-bruce-hansen-2014.pdf",
  "ROM": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\b81821bd16a42211f919748c26cd0774.pdf",
  "PIN": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global Edition (2017, Pearson Education Limited) - libgen.li.pdf",
  "MAD": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\international-financial-management-11th-edition-by-jeff-madura.pdf",
}

out = []
for code, p in pdfs.items():
    try:
        doc = fitz.open(p)
        toc = doc.get_toc()
        chapters = []
        for level,title,page in toc:
            if level == 1:
                chapters.append({"level":level,"title":title,"page":page})
        out.append({"code":code,"total_pages":len(doc),"toc_count":len(toc),"chapters_level1":chapters[:30]})
        doc.close()
    except Exception as e:
        out.append({"code":code,"err":str(e)})
Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\docs\toc_summary.json").write_text(json.dumps(out,indent=2,ensure_ascii=False), encoding="utf-8")
print(json.dumps(out))
