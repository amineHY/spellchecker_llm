"""
Spellchecker using LLM
"""

import logging
from string import Template
import time

from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

controller = Controller()
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "mistral:7b-instruct-v0.2-q4_K_S",
    "stream": False,
}
PROMPT_TEMPLATE = Template(
    """Fix all typos, punctuation and casing in this text, but preserve all new line characters:

$text

Return only the corrected text and do not include the preamble.
"""
)


def spellcheck_with_llm(text):
    """Spellcheck text using Ollama API."""
    logger.info("Fixing selected text using Ollama")
    prompt = PROMPT_TEMPLATE.substitute({"text": text})
    logger.info(f"Prompt = {prompt}")
    try:
        response = requests.post(
            OLLAMA_ENDPOINT,
            json={
                "model": OLLAMA_CONFIG["model"],
                "stream": OLLAMA_CONFIG["stream"],
                "prompt": prompt,
            },
            timeout=5,
        )
        response.raise_for_status()
        response_json = response.json()
        logger.debug(f"Full response: {response_json}")

        # Check if the response is as expected
        if "response" in response_json:
            fixed_text = response_json["response"].strip('"')
        else:
            logger.error(
                f"Unexpected response from Ollama API: {response_json}"
            )
            return text

        logger.debug(f"Response: {fixed_text}")
        return fixed_text

    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with Ollama API: {e}")
        logger.error(
            f"Response content: {response.content}"
        )  # Log the response content for debugging
        return text


def fix_selected_text():
    """Fix selected text."""
    # Copy current selection to clipboard
    with controller.pressed(Key.cmd):
        controller.tap("c")
    time.sleep(0.1)  # Added a small delay

    # Get text from clipboard
    text = pyperclip.paste()
    logger.debug(f"Original text: {text}")

    # Fix text with LLM
    fixed_text = spellcheck_with_llm(text)
    logger.info(f"Fixed text: {fixed_text}")

    # Copy fixed text back to clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)  # Added a small delay

    # Paste fixed text
    with controller.pressed(Key.cmd):
        controller.tap("v")


# Hotkey listener
def on_f9():
    """Handle F9 keypress."""
    logger.info("F9 key pressed")
    fix_selected_text()


def on_f10():
    """Handle F10 keypress."""
    logger.info("F10 key pressed")
    fix_selected_text()


def main():
    """Main function."""
    logger.info("Spell Checker Running ...")
    with keyboard.GlobalHotKeys({"<101>": on_f9, "<109>": on_f10}) as h:
        h.join()


if __name__ == "__main__":
    main()