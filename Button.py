import pynput as pn
import keyboard as kb

class Button:
    def __init__(self):
        self.key = ''
        self.pos = None
        self.is_pressed = False

    def set_key(self, hotkey):
        self.key = hotkey

    def set_pos(self, position):
        self.pos = position