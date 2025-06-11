import os
import openai
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

#API key 
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file or environment variables")

client = OpenAI(api_key=api_key)

#system and user messages
system_prompt = {
    "role": "system",
    "content": "You are a assistant that explains things clearly and simply."
}

user_input = input("User: ")
user_prompt = {
    "role": "user",
    "content": user_input
}

#API calling
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, user_prompt]
)

#assistant reply
assistant_reply = response.choices[0].message.content
print("\nAssistant:", assistant_reply)

#token usage
print("\nToken Usage:", response.usage)
