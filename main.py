import keyboard
import pyperclip

copied_texts = {}

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('c') and keyboard.is_pressed('1'):
        copied_texts['1'] = pyperclip.paste()
        print('Text copied to 1:', copied_texts['1'])

    elif e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('c') and keyboard.is_pressed('2'):
        copied_texts['2'] = pyperclip.paste()
        print('Text copied to 2:', copied_texts['2'])

    elif e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('b') and keyboard.is_pressed('1'):
        pyperclip.copy(copied_texts.get('1', ''))
        keyboard.press_and_release('ctrl+v')

    elif e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl') and keyboard.is_pressed('b') and keyboard.is_pressed('2'):
        pyperclip.copy(copied_texts.get('2', ''))
        keyboard.press_and_release('ctrl+v')

keyboard.hook(on_key_event)

keyboard.wait()

