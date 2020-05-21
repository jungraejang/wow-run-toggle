from pynput import keyboard
import pyautogui


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char="w")},
    {keyboard.Key.shift, keyboard.KeyCode(char="W")}
]

current = set()

def execute():
    # print("activated")
    pyautogui.keyDown('w')

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()