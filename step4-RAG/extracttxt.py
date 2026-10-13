from pypdf import PdfReader

reader = PdfReader("samplepayroll.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

print(text[:1000])
