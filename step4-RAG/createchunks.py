from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader



reader = PdfReader("samplepayroll.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

print("=======================================")
print("extracted text below 20 words")
print(text[:20])
print("=======================================")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:2]):
    print(f"\nChunk {i}")
    print("=======================================")
    print("Below chunk")
    print(chunk)
