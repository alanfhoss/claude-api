from dotenv import load_dotenv
from anthropic import Anthropic

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def stream_chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 16000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    with client.messages.stream(**params) as stream:
        for event in stream:
            print(event)
        final_message = stream.get_final_message()
    # for block in response.content:
    #     if block.type == "thinking":
    #         print("Thinking:", block.thinking)
    #         output = block.thinking
    #     elif block.type == "redacted_thinking":
    #         pass  # encrypted; nothing readable
    #     elif block.type == "text":
    #         print(block.text)
    #         output = block.text
    # return output
    return final_message

load_dotenv()
client = Anthropic()
model = "claude-opus-5-5"

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define three aspects of quantum computing as they relate to cybersecurity")

# Get Claude's response
finalanswer = stream_chat(messages)

print(finalanswer.content)

# Add Claude's response to the conversation history
add_assistant_message(messages, finalanswer.content)