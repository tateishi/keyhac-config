#from pathlib import Path

#import pyauto
#from keyhac import *


EDITOR = "notepad.exe"
FONT = "HackGenNerd Console"
FONT_SIZE = 16

modifiers = [
    (235, "User0", "U0"),
    (236, "User1", "U1"),
    (237, "User2", "U2"),
    (238, "User3", "U3"),
    (239, "User4", "U4"),
]


def make_keymap(map, id, modifiers=modifiers):
    number, name, prefix = modifiers[id]
    d = { f"{prefix}-{k}": v for k, v in map.items() }
    return d


def set_keys(keymap, map, keymap_dict, modifier_key, id, one_shot=True):
    number, name, prefix = modifiers[id]
    keymap.replaceKey(modifier_key, number)
    keymap.defineModifier(number, name)
    keymap_dict = make_keymap(keymap_dict, id)

    if one_shot:
        map[f"O-({number})"] = modifier_key

    for k, v in keymap_dict.items():
        map[k] = v


def muhenkan_map(keymap):
    keymap_dict = {
        "h": "Left",
        "j": "Down",
        "k": "Up",
        "l": "Right",

        "C-h": "Home",
        "C-j": "PageDown",
        "C-k": "PageUp",
        "C-l": "End",

        "S-h": "S-Left",
        "S-j": "S-Down",
        "S-k": "S-Up",
        "S-l": "S-Right",

        "C-S-h": "S-Home",
        "C-S-j": "S-PageDown",
        "C-S-k": "S-PageUp",
        "C-S-l": "S-End",

        "Enter": "Esc",
        "Space": "Back",

        "b": "(1)",   # MOUSE_LBUTTON
        "n": "(166)", # BROWSER_BACKWARD
        "m": "(167)", # BROWSER_FORWARD
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "(29)", 0)


def space_map(keymap):
    keymap_dict = {
        "h": "Left",
        "j": "Down",
        "k": "Up",
        "l": "Right",

        "C-h": "Home",
        "C-j": "PageDown",
        "C-k": "PageUp",
        "C-l": "End",

        "S-h": "S-Left",
        "S-j": "S-Down",
        "S-k": "S-Up",
        "S-l": "S-Right",

        "C-S-h": "S-Home",
        "C-S-j": "S-PageDown",
        "C-S-k": "S-PageUp",
        "C-S-l": "S-End",

        "Enter": "Esc",
        "Period": "Space",
        "Comma": "Back",
 
        "s": "s-7",  # SINGLE QUOTE
        "d": "s-2",  # DOUBLE QUOTE
        "a": "s-BackQuote",  # BACK QUOTE

        "i":   "s-8",  # LEFT PAREN
        "o":   "s-9",  # RIGHT PAREN
        "s-i": "s-Comma",  # LEFT ANLE BRACKET
        "s-o": "s-Period",  # RIGHT ANGLE BRACKET
        "p":      "OpenBracket",  # LEFT BRACKET
        "Atmark": "CloseBracket",  # RIGHT BRACKET
        "s-p":      "s-OpenBracket",  # LEFT CURLY BRACKET
        "s-Atmark": "s-CloseBracket",  # RIGHT CURLY BRACKET

        "b": "(1)",   # MOUSE_LBUTTON
        "n": "(166)", # BROWSER_BACKWARD
        "m": "(167)", # BROWSER_FORWARD
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "space", 0)


def set_globalmap(keymap):
    space_map(keymap)
#    muhenkan_map(keymap)


def configure(keymap):
    keymap.editor = EDITOR

    # Font
    keymap.setFont(FONT, FONT_SIZE)

    # Theme
    keymap.setTheme("black")

    set_globalmap(keymap)