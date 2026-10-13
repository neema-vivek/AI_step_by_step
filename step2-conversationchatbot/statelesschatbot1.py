from openai import AzureOpenAI

# Azure OpenAI Configuration
client = AzureOpenAI(
    api_key="<apikey>",
    api_version="2024-12-01-preview",
    azure_endpoint="https://testfoundry.services.ai.azure.com/"
)

DEPLOYMENT_NAME = "gpt-4o"

print("Stateless Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    print(f"\nAssistant: {answer}\n")

print(response.choices[0].message.content)
