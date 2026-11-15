# Quickstart — First Content in 5 Minutes

## 1. Get an API key

Pick one provider and get a key:

- OpenAI — https://platform.openai.com/api-keys
- Anthropic — https://console.anthropic.com
- Gemini — https://aistudio.google.com/apikey

## 2. Set up your environment

Copy `.env.example` to `.env` and paste your key:

    Copy-Item .env.example .env

## 3. Install dependencies (Python example)

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install openai python-dotenv

## 4. Generate your first draft

    python tools\openai\generate.py

## 5. Or use a prompt template manually

Open `prompts/drafting/blog-post.md`, fill the `{{variables}}`, paste into
your model's chat. Done.

## Next

- Explore `docs/guides/prompting-guide.md`
- Automate with `automation/workflows/blog-pipeline.md`
- Browse more prompts in `prompts/`
