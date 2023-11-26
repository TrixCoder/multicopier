# Multicopier

Multicopier is a simple Python script that enables users to copy and paste multiple texts using customizable keyboard shortcuts. This project utilizes the `keyboard` and `pyperclip` libraries to achieve the desired functionality.

## Features

- **Customizable Shortcuts:** Users can define their own keyboard shortcuts for copying and pasting texts to different slots.
- **Multiple Slots:** The multicopier supports multiple slots (e.g., Slot 1, Slot 2, ..., Slot 10) for storing and retrieving copied texts.
- **Clipboard Interaction:** The script interacts with the clipboard using the `pyperclip` library to ensure seamless copying and pasting.

## Usage

1. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the script:**
    ```bash
    python main.py
    ```

3. **Copying Text:**
    - Press `Ctrl + C + 1` to copy the current text to Slot 1.
    - Press `Ctrl + C + 2` to copy the current text to Slot 2.
    - Repeat this process for other slots as needed.

4. **Pasting Text:**
    - Press `Ctrl + B + 1` to paste the text from Slot 1.
    - Press `Ctrl + B + 2` to paste the text from Slot 2.
    - Repeat this process for other slots as needed.

## Customization

Users can customize the keyboard shortcuts by modifying the `on_key_event` function in the `main.py` file. The script is designed to handle up to 10 slots, and additional slots can be added as required.

## Requirements

```plaintext
keyboard
pyperclip
```

## Installation

Install the required libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Notes

- Ensure that the script is run in an environment where the `keyboard` library can interact with the keyboard events.

