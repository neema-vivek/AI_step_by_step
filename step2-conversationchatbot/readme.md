# Adding Conversation Memory to an LLM Application

## Introduction

In the previous article, we learned how to connect to an LLM and generate responses using the Chat Completion API.

One limitation of a basic LLM application is that it is stateless. The model does not remember previous interactions unless the application sends them again.

In this article, we will explore different approaches to maintaining conversation context and memory.

We will implement:

1. Stateless Chatbot
2. Stateful Chatbot
3. Sliding Window Memory (Last 20 Messages)

---

## Goal

Understand how conversational memory works and learn different approaches for maintaining context in chatbot applications.

---

## Understanding Conversation Memory

LLMs do not remember previous API calls.

Every request sent to the model is processed independently.

If we want a chatbot to remember past conversations, our application must maintain and resend conversation history.

---

## Memory Approaches

### 1. Stateless Conversation

A stateless chatbot sends only the current question to the model.

#### Flow

```text
User Question
      ↓
     LLM
      ↓
Response
```

#### Characteristics

- Simple to implement
- Lowest token usage
- Lowest cost
- No memory
- No conversation context

#### Example

User:

```text
My name is Vivek
```

Assistant:

```text
Nice to meet you Vivek.
```

User:

```text
What is my name?
```

Assistant:

```text
I don't know because your previous message was not provided.
```

#### File

```text
stateless_chat.py
```

---

### 2. Stateful Conversation

A stateful chatbot stores conversation history and sends it with every request.

#### Flow

```text
Chat History
      +
Current Question
      ↓
      LLM
      ↓
Response
```

#### Characteristics

- Remembers previous messages
- Supports multi-turn conversations
- Better user experience
- Token usage grows over time
- Cost increases as history grows

#### Example

User:

```text
My name is Vivek
```

Assistant:

```text
Nice to meet you Vivek.
```

User:

```text
What is my name?
```

Assistant:

```text
Your name is Vivek.
```

#### How It Works

Conversation history is stored in a list:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]
```

Each user message and assistant response is added to this list.

The entire history is sent to the LLM during every request.

#### File

```text
stateful_chat.py
```

---

### 3. Sliding Window Memory

As conversations become longer, sending the entire chat history becomes expensive and may exceed the model's context window.

A common solution is to keep only the most recent messages.

#### Flow

```text
Recent Messages
      +
Current Question
      ↓
      LLM
      ↓
Response
```

#### Example

Keep only the last:

```text
20 Messages
```

When a new message arrives:

```text
Oldest Message
        Removed

Newest Message
        Added
```

#### Benefits

- Controls token usage
- Reduces API cost
- Prevents context window issues
- Maintains recent conversation context

#### Limitations

Older information is eventually forgotten.

Example:

```text
Message 1:
My name is Vivek
```

After 100 messages:

```text
What is my name?
```

The chatbot may no longer remember because the original message was removed from memory.

#### File

```text
sliding_window_chat.py
```

---

## Comparing the Approaches

### Stateless

Memory: No

Cost: Low

Context Awareness: No

---

### Stateful

Memory: Yes

Cost: Increases as conversation grows

Context Awareness: High

---

### Sliding Window

Memory: Partial

Cost: Controlled

Context Awareness: Recent conversations only

---

## Context Window

Every LLM has a maximum amount of information it can process in a single request.

This limit is called the Context Window.

The context window contains:

- System Messages
- User Messages
- Assistant Messages
- Retrieved Documents (RAG)

As conversations grow, they consume more of the available context window.

---

## Token Usage

LLMs process text as tokens rather than words.

Total request cost is based on:

```text
Input Tokens
+
Output Tokens
=
Total Tokens
```

More conversation history results in:

- More tokens
- Higher cost
- Increased latency

---

## Project Structure

```text
Article-02-Conversation-Memory/
│
├── stateless_chat.py
├── stateful_chat.py
├── sliding_window_chat.py
└── README.md
```

---

## Key Takeaways

- LLMs are naturally stateless.
- Applications create memory by storing conversation history.
- Stateful chatbots provide better conversational experiences.
- Token usage grows as chat history grows.
- Sliding Window Memory limits token consumption by keeping only recent messages.
- Long conversations require memory management techniques.

---

## Next Steps

In the next article, we will explore more advanced memory strategies:

- Conversation Summarization
- Long-Term Memory
- Semantic Memory
- Embeddings
- Memory Retrieval

These concepts will prepare us for building Retrieval-Augmented Generation (RAG) applications and AI Agents.
