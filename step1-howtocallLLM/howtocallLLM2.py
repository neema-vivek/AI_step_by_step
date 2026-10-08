from openai import AzureOpenAI

# Azure OpenAI Configuration
client = AzureOpenAI(
    api_key="<put your key here>",
    api_version="2024-12-01-preview",
    azure_endpoint="https://<yourfoundryname>.services.ai.azure.com/"
)

# Send prompt to LLM
response = client.chat.completions.create(
    model="gpt-4o",  # Azure deployment name
    messages=[
        {
            "role": "user",
            "content": "What is Kubernetes?"
        },
        {
                    "role": "system",
                    "content": "you are kubernetes expert , give answers only in one line"
          }
    ]
)

# Print response
print(response.choices[0].message.content)
