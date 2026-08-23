import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("knowledge/profile.json", "r", encoding="utf-8") as file:
    profile = json.load(file)


SYSTEM_PROMPT = f"""
You are Dhruv AI, the personal AI assistant for Dhruv Budhwani.

Your job is to help visitors understand Dhruv's:
- education
- skills
- projects
- experience
- technical interests

Only use the information provided in Dhruv's profile below.

Do not invent information.

If the information is not available, say that you don't have
that information.

Keep your answers clear and concise.

Dhruv's profile:

{json.dumps(profile, indent=2)}
"""


def ask_agent(message):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
{SYSTEM_PROMPT}

Visitor's question:
{message}
"""
    )

    return response.text


if __name__ == "__main__":
    question = input("Ask Dhruv AI: ")

    answer = ask_agent(question)

    print("\nDhruv AI:")
    print(answer)
    print("GEMINI KEY EXISTS:", bool(os.getenv("GEMINI_API_KEY")))