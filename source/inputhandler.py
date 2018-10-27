from kivy.logger import Logger

class InputHandler(object):
    def __init__(self, kivyroot):
        self.kivyroot = kivyroot
    
    def parse_input(self, keyboard, key, scancode=None, codepoint=None, modifier=None, **kwargs):
        Logger.info("input: " + str(repr(key)) + ", sc: " + str(repr(scancode)) + ", codepoint: " + str(repr(codepoint)) + ", mods: " + str(repr(modifier)))
