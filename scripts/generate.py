# generate.py — call an LLM to generate content
# Requires: OPENAI_API_KEY in environment (.env, gitignored)

import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate(prompt: str) -> str:
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    print(generate("Write a short intro about AI content engines."))
