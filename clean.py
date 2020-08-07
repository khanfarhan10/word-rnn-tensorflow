import re

def clean_text(string):
    pattern = "(page|PAGE|Page)(\s+\|\s+)([0-9]+)(.*)$"
    output_cleaned = re.sub("\s$", "", string, flags=re.MULTILINE)
    p = re.compile(pattern, re.MULTILINE)
    output_cleaned = p.sub(" ", output_cleaned)
    return output_cleaned

with open("input.txt","r", encoding="cp437", errors="ignore") as f, open("output.txt","w", encoding="cp437", errors="ignore") as g:
    string = f.read()
    cleaned_text = clean_text(string)
    g.write(cleaned_text)