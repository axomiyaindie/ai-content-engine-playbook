"""Generate content with the OpenAI API.

Usage:
    pip install openai python-dotenv
    set OPENAI_API_KEY in .env
    python tools/openai/generate.py
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

PROMPT_FILE = Path(__file__).resolve().parents[2] / "prompts" / "drafting" / "blog-post.md"


def load_prompt() -> str:
    template = PROMPT_FILE.read_text(encoding="utf-8")
    values = {
        "{{topic}}": "AI content pipelines",
        "{{audience}}": "marketing teams",
        "{{tone}}": "practical, no-fluff",
        "{{word_count}}": "900",
        "{{keyword}}": "ai content engine",
        "{{outline}}": "1. Why pipelines matter\n2. How to build one\n3. Common mistakes",
    }
    for key, value in values.items():
        template = template.replace(key, value)
    return template


def generate(prompt: str, model: str = "gpt-4o-mini") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(generate(load_prompt()))
