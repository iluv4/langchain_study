import json
import openai

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "아기야 뭐하노"
        }
    ],
    max_tokens = 100,
    temperature=1,
    n=2,
)

print(json.dumps(response, indent=2, ensure_ascii=False))