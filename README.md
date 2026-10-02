# daily_dish

A small terminal chat app backed by Groq.

## Setup

```
uv sync
cp .env.example .env   # then add your GROQ_API_KEY
```

## Run

```
uv run daily-dish
# or
uv run python -m daily_dish
```

## Layout

- `src/daily_dish/` - the package (`cli.py` chat loop, `llm.py` Groq client)
- `notebooks/` - course notebooks
- `docs/` - reference material
