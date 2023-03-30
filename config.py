#from pathlib import Path

#import pyauto
#from keyhac import *


EDITOR = "notepad.exe"
FONT = "HackGenNerd Console"
FONT_SIZE = 16


def set_keys(keymap, map, keymap_dict, modifier_key, id, user_key, one_shot=True):
    keymap.replaceKey(modifier_key, id)
    keymap.defineModifier(id, user_key)

    if one_shot:
        map[f"O-({id})"] = modifier_key

    for k, v in keymap_dict.items():
        map[k] = v


def set_globalmap(keymap):
    keymap_dict = {
        "U0-h": "Left",
        "U0-j": "Down",
        "U0-k": "Up",
        "U0-l": "Right",

        "U0-C-h": "Home",
        "U0-C-j": "PageDown",
        "U0-C-k": "PageUp",
        "U0-C-l": "End",

        "U0-S-h": "S-Left",
        "U0-S-j": "S-Down",
        "U0-S-k": "S-Up",
        "U0-S-l": "S-Right",

        "U0-C-S-h": "S-Home",
        "U0-C-S-j": "S-PageDown",
        "U0-C-S-k": "S-PageUp",
        "U0-C-S-l": "S-End",

        "U0-Enter": "Esc",
        "U0-Space": "Back",

        "U0-b": "(1)",   # MOUSE_LBUTTON
        "U0-n": "(166)", # BROWSER_BACKWARD
        "U0-m": "(167)", # BROWSER_FORWARD
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "(29)", 235, "User0")


def configure(keymap):
    keymap.editor = EDITOR

    # Font
    keymap.setFont(FONT, FONT_SIZE)

    # Theme
    keymap.setTheme("black")

    set_globalmap(keymap)