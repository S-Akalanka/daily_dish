# Pedal Pal

A small terminal chat app backed by Groq.

## Setup

```
uv sync
cp .env.example .env   # then add your GROQ_API_KEY
```

## Run

```
uv run pedal-pal
# or
uv run python -m pedal_pal
```

## Layout

- `src/pedal_pal/` - the package (`cli.py` chat loop, `llm.py` Groq client)
- `notebooks/` - course notebooks
- `docs/` - reference material
