import fitz
pdfs = {'ROM': r'C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\b81821bd16a42211f919748c26cd0774.pdf','PIN': r'C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global Edition (2017, Pearson Education Limited) - libgen.li.pdf','MAD': r'C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\international-financial-management-11th-edition-by-jeff-madura.pdf'}
for code,p in pdfs.items():
    print('===',code,'===')
    doc=fitz.open(p)
    toc=doc.get_toc()
    for level,title,page in toc:
        t=title.lower()
        if level<=2 and ('chapter' in t or t.startswith('part')):
            print(level,title,page)
    print()
    doc.close()
