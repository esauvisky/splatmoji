#!/usr/bin/env python3
"""
Small script that sends Shift+Insert to bypass xdotool lag on Gnome/GTK3 environments
"""

__author__ = "Emi Bemol"
__version__ = "0.2"
__license__ = "MIT"

from pynput.keyboard import Key, Controller

keyboard = Controller()
with keyboard.pressed(Key.shift):
    keyboard.press(Key.insert)
    keyboard.release(Key.insert)
