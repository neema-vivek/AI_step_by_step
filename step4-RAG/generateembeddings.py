import os
from openai import AzureOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

# ---------------------------------------------------------------------------
# 1. Extract text from the PDF
# ---------------------------------------------------------------------------
reader = PdfReader("samplepayroll.pdf")

text = ""
for page in reader.pages:
    text += (page.extract_text() or "") + "\n"

print("=======================================")
print("extracted text (first 200 chars)")
print(text[:200])
print("=======================================")

# ---------------------------------------------------------------------------
# 2. Split into chunks
# ---------------------------------------------------------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)
print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:1]):
    print(f"\nChunk {i}")
    print("=======================================")
    print(chunk)

# ---------------------------------------------------------------------------
# 3. Create the Azure OpenAI client
#    - azure_endpoint is the RESOURCE root (no /api/projects/... path)
#    - api_version is REQUIRED by Azure
#    - the "model" argument below must be your DEPLOYMENT name, which may or
#      may not be the same as the base model name "text-embedding-3-small"
# ---------------------------------------------------------------------------
client = AzureOpenAI(
    azure_endpoint="https://testfoundry.services.ai.azure.com",
    api_key=os.environ.get("AZURE_OPENAI_API_KEY", "xxxxxx"),
    api_version="2024-10-21",
)

# This must match the DEPLOYMENT name you created in the Azure portal /
# AI Foundry, not necessarily the base model name.
embedding_deployment = "text-embedding-3-small"

# ---------------------------------------------------------------------------
# 4. Generate embeddings
# ---------------------------------------------------------------------------
documents = []

for idx, chunk in enumerate(chunks):
    response = client.embeddings.create(
        model=embedding_deployment,
        input=chunk,
    )
    embedding = response.data[0].embedding

    documents.append({
        "id": str(idx),
        "content": chunk,
        "embedding": embedding,
    })

print(f"\nGenerated embeddings for {len(documents)} chunks")
print(f"Embedding dimension: {len(documents[0]['embedding']) if documents else 0}")
