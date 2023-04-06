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


def muhenkan_map(keymap):
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
        "U0-Period": "Space",
        "U0-Comma": "Back",

        "U0-s": "s-7",  # SINGLE QUOTE
        "U0-d": "s-2",  # DOUBLE QUOTE

        "U0-i":   "s-8",  # LEFT PAREN
        "U0-o":   "s-9",  # RIGHT PAREN
        "U0-s-i": "s-Comma",  # LEFT ANGLE BRACKET
        "U0-s-o": "s-Period",  # RIGHT ANGLE BRACKET
        "U0-p":      "OpenBracket",  # LEFT BRACKET
        "U0-Atmark": "CloseBracket",  # RIGHT BRACKET
        "U0-s-p":      "s-OpenBracket",  # LEFT CURLY BRACKET
        "U0-s-Atmark": "s-CloseBracket",  # RIGHT CURLY BRACKET

        "U0-slash": "Apps", # Application Key

        "U0-b": "(1)",   # MOUSE_LBUTTON
        "U0-n": "(166)", # BROWSER_BACKWARD
        "U0-m": "(167)", # BROWSER_FORWARD
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "(29)", 235, "User0")


def space_map(keymap):
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
        "U0-Period": "Space",
        "U0-Comma": "Back",

        "U0-s": "s-7",  # SINGLE QUOTE
        "U0-d": "s-2",  # DOUBLE QUOTE

        "U0-i":   "s-8",  # LEFT PAREN
        "U0-o":   "s-9",  # RIGHT PAREN
        "U0-s-i": "s-Comma",  # LEFT ANGLE BRACKET
        "U0-s-o": "s-Period",  # RIGHT ANGLE BRACKET
        "U0-p":      "OpenBracket",  # LEFT BRACKET
        "U0-Atmark": "CloseBracket",  # RIGHT BRACKET
        "U0-s-p":      "s-OpenBracket",  # LEFT CURLY BRACKET
        "U0-s-Atmark": "s-CloseBracket",  # RIGHT CURLY BRACKET

        "U0-slash": "Apps", # Application Key

        "U0-b": "(1)",   # MOUSE_LBUTTON
        "U0-n": "(166)", # BROWSER_BACKWARD
        "U0-m": "(167)", # BROWSER_FORWARD
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "space", 235, "User0")


def ro_map(keymap):
    keymap_dict = {
        "U1-h": "Left",
        "U1-j": "Down",
        "U1-k": "Up",
        "U1-l": "Right",

        "s-(236)": "_",
    }

    map = keymap.defineWindowKeymap()
    set_keys(keymap, map, keymap_dict, "backslash", 236, "User1")



def set_globalmap(keymap):
#    space_map(keymap)
    muhenkan_map(keymap)
    ro_map(keymap)


def configure(keymap):
    keymap.editor = EDITOR

    # Font
    keymap.setFont(FONT, FONT_SIZE)

    # Theme
    keymap.setTheme("black")

    set_globalmap(keymap)