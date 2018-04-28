# Twitter markov bot

## Installation

```
pip install requirements.txt
```

Then make a copy of `config.example.json`, named `config.json`.

## Usage

```
python tweet.py
```

## Packaging it up for Lambda

You need dependencies to be installed at the top level, so:

```
pip install -r requirements.txt -t .
```