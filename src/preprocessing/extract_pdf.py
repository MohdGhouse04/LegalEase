from pypdf import PdfReader
import json

reader = PdfReader("data/raw/constitution_of_india.pdf")

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

with open("data/processed/constitution_text.json","w") as f:
    json.dump({"text":full_text},f)

print("Characters extracted:", len(full_text))