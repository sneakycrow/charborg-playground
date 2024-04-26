# charborg-playground

A collection of tools, scripts, and other tech for Charborg to use while streaming on Twitch

## Requirements

- Python 3.12
- Justfile [optional]

## Installation

Install dependencies from the requirements

Using `just`

```sh
just install
```

Using `python`

```sh
pip install -r requirements.txt
```

## Running

The default formula runs the save_emotes function which will save all emotes to a csv file

Using `just`:

```sh
just save_emotes
```

Or run it based on the default formula

```sh
just
```

Using `python`:

```sh
python main.py
```
