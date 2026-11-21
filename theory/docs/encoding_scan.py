#!/usr/bin/env python3
import os,json
from pathlib import Path
base=Path(r'C:\Users\PC\Documents\AI_project\sandbox-financial\theory')
exts={'.py','.yaml','.yml','.json','.jsonl','.md','.csv','.txt'}
files=[]
for root,dirs,fnames in os.walk(base):
    for fn in fnames:
        p=Path(root)/fn
        if p.suffix.lower() in exts: files.append(p)
res=[]
for p in files:
    info={'path':str(p),'bom':False,'utf8_ok':False,'err':None,'has_mojibake_like':False}
    try:
        raw=p.read_bytes()
        if raw.startswith(b'\xef\xbb\xbf'): info['bom']=True
        try:
            txt=raw.decode('utf-8')
            info['utf8_ok']=True
            if 'Ãƒ' in txt or 'Ã‚' in txt or 'Ã¢â‚¬â„¢' in txt or 'Ã¢â‚¬Å“' in txt or '\ufffd' in txt: info['has_mojibake_like']=True
        except Exception as e:
            info['err']=str(e)
    except Exception as e:
        info['err']=str(e)
    res.append(info)
out=Path(r'C:\Users\PC\Documents\AI_project\sandbox-financial\theory\docs\encoding_scan.json')
out.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'count':len(res),'errors':sum(1 for x in res if not x['utf8_ok']),'bom':sum(1 for x in res if x['bom']),'mojibake_like':sum(1 for x in res if x['has_mojibake_like'])}))
