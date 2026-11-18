from dotenv import load_dotenv
from anthropic import Anthropic

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    response = client.messages.create(**params)

    for block in response.content:
        if block.type == "thinking":
            print("Thinking:", block.thinking)
            output = block.thinking
        elif block.type == "redacted_thinking":
            pass  # encrypted; nothing readable
        elif block.type == "text":
            print(block.text)
            output = block.text
    return output

load_dotenv()
client = Anthropic()
model = "claude-opus-5-5"

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

print(answer)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Give me one more sentence on this")

# Get the follow-up response with full context
final_answer = chat(messages)

print(final_answer)