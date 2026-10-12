from openai import AzureOpenAI

# Azure OpenAI Configuration
client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-12-01-preview",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com/"
)

DEPLOYMENT_NAME = "gpt-4o"

# Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("Stateful Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message to history
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    # Add assistant response to history
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    print(f"\nAssistant: {assistant_reply}\n")
