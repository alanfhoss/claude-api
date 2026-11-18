from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]

)

print(message.content[0].text)
print(message)
