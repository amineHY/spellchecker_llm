# Check Spelling of a selected text accros OS

- [Check Spelling of a selected text accros OS](#check-spelling-of-a-selected-text-accros-os)
  - [Install The Project](#install-the-project)
  - [Export a requirements file](#export-a-requirements-file)
  - [Run the project](#run-the-project)
  - [Usage](#usage)

## Install The Project

    poetry install

## Export a requirements file

```
poetry export --format=requirements.txt --output=requirements.txt --without-hashes
```

pyright spellchecker_llm/script.py

## Run the project

Activate python environment

    poetry shell

Running the project

    (spellchecker-llm-py3.11) ➜  spellchecker_llm git:(main) ✗ python spellchecker_llm/script.py
    INFO:__main__:Spell Checker Running ...
    INFO:__main__:F9 key pressed
    INFO:__main__:Fixing selected text using Ollama
    INFO:__main__:Prompt = Fix all typos, punctuation and casing in this text, but preserve all new line characters:

## Usage

- Leave the project running in the terminal
- Select a text (across any app of your OS) and you would like to correct
- Type F9 (e.g. fn + F9 on mac) to trigger. Correction, have fun.
