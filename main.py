import keyboard
import pyperclip

copied_texts = {}

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('c') and e.name.isdigit():
        slot_key = e.name
        copied_texts[slot_key] = pyperclip.paste()
        print(f'Text copied to Slot {slot_key}:', copied_texts[slot_key])

    elif e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('b') and e.name.isdigit():
        slot_key = e.name
        pyperclip.copy(copied_texts.get(slot_key, ''))
        keyboard.press_and_release('ctrl+b')

keyboard.hook(on_key_event)

keyboard.wait()
