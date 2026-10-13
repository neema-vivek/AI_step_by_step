from openai import AzureOpenAI

# Azure OpenAI Configuration
client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-12-01-preview",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com/"
)

DEPLOYMENT_NAME = "gpt-4o"

MAX_MESSAGES = 20

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("Sliding Window Chatbot Started")
print("Only the last 20 messages will be remembered.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Keep system prompt + last 20 messages
    messages = [messages[0]] + messages[-MAX_MESSAGES:]

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    # Add assistant response
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    # Again trim history
    messages = [messages[0]] + messages[-MAX_MESSAGES:]

    print(f"\nAssistant: {assistant_reply}\n")

    print(f"Current Messages Stored: {len(messages)}")
