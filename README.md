# Trail Pal

A terminal chat assistant for **Trail Pal**, a fictional outdoor tours company in Nuwara Eliya, Sri Lanka (guided hikes, Horton Plains treks and kayaking on Lake Gregory).

It answers common questions from an FAQ PDF using basic TF-IDF matching, and hands everything else to an LLM that also knows today's weather.

## Features

* **FAQ answers from a PDF.** Questions about tours, prices, booking and policies are matched against `docs/faqs.pdf` with TF-IDF and cosine similarity. These answers are instant, free and exactly as written.
* **LLM fallback.** When no FAQ is similar enough, the question goes to an LLM (Groq) guided by a system prompt in `docs/instructions.md`.
* **Live weather.** If the question mentions weather (rain, hot, cold, forecast, and so on), the current weather for Nuwara Eliya is fetched from OpenWeather and given to the LLM, so it can say whether a tour is likely to run.
* **Conversation memory.** The whole chat, including FAQ answers and weather readings, is kept in a history list and sent with every LLM call, so follow up questions like "say that again" or "was it colder earlier?" work.

Weather is **today only**. There are no forecasts.

## How it works

```
user question
    |
    v
FAQ matcher (TF-IDF + cosine similarity)
    |
    |-- similarity >= 0.45 --> print the FAQ answer
    |
    '-- similarity <  0.45 --> weather keyword in the question?
                                  |-- yes --> fetch current weather, add it to history
                                  '-- no  --> (nothing extra)
                               send the history + system prompt to the LLM
                               print the reply
```

## Project structure

```
course_era1/
├── docs/
│   ├── faqs.pdf              FAQ knowledge base (Q and A pairs)
│   └── instructions.md       System prompt: company facts and answering rules
├── notebooks/                Original course notebook (reference only)
├── src/trail_pal/
│   ├── main.py               Entry point: loads the FAQ and starts the chat
│   ├── cli.py                Chat loop, routing, weather keyword check
│   ├── tools/
│   │   ├── faqAgent.py       TF-IDF FAQ matcher
│   │   ├── weather.py        OpenWeather client
│   │   └── memoryAgent.py    Stores chat history and the last weather reading
│   └── utils/
│       ├── load.py           Reads text from the PDF
│       ├── clean.py          Collapses whitespace
│       ├── parse.py          Extracts Q and A pairs with a regex
│       └── llm.py            Groq chat completion call
├── .env.example              Template for API keys
├── pyproject.toml
└── README.md
```

## Setup

### Requirements

* Python 3.14 or newer
* [uv](https://docs.astral.sh/uv/) (package manager)
* A free [Groq API key](https://console.groq.com/keys)
* A free [OpenWeather API key](https://home.openweathermap.org/api_keys)

### Install

```bash
git clone <your repo url>
cd <repo folder>
uv sync
```

### Configure API keys

Copy the example file and fill in your keys:

```bash
cp .env.example .env          # macOS or Linux
copy .env.example .env        # Windows (cmd)
```

Then edit `.env`:

```
GROQ_API_KEY=your_groq_key
OPEN_WEATHER=your_openweather_key
```

Never commit `.env`. It is already listed in `.gitignore`. New OpenWeather keys can take a short while to activate.

### Run

```bash
uv run trail-pal
```

Type `exit` to quit.

## Example

```
You       : how much does a tour cost
Assistant : Half day hikes are 45 dollars, full day treks are 85 dollars, and kayak trips are 60 dollars per person...

You       : hows the weather
Assistant : Few clouds and 11 degrees in Nuwara Eliya, well within our limits, so tours should run today...

You       : say that again
Assistant : (repeats the previous answer, because it is in the history)
```

## Customising

| What | Where |
|---|---|
| Replace the FAQ | Edit `docs/faqs.pdf`. Entries must look like `1. Q: question` then `A: answer`, numbered, one after another. |
| Company facts and tone | `docs/instructions.md` |
| Match strictness | The similarity threshold in `src/trail_pal/tools/faqAgent.py` (default 0.45). Raise it for fewer FAQ matches, lower it for more. |
| Weather location | `LOCATION` in `src/trail_pal/cli.py` |
| Weather keywords | `weather_keywords` in `src/trail_pal/cli.py` |
| LLM model | `MODEL` in `src/trail_pal/utils/llm.py` |

## Limitations

* TF-IDF does not understand meaning, only shared words.
* Weather is the current reading for one location, with no forecast.
* Weather routing uses simple substring keywords, so a word like "hot" can also match inside other words.
* Chat history lives in memory and is lost when the program exits. It also grows for the length of the session.
* The FAQ must keep the numbered `N. Q:` and `A:` format, or the parser will not find the entries.
