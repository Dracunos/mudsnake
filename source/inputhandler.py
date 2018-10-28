from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.widget import Widget

class InputHandler(object):
    def __init__(self, kivyroot):
        self.kivyroot = kivyroot
    
    def parse_input(self, keyboard, key, scancode=None, codepoint=None, modifier=None, **kwargs):
        Logger.info("Input: " + str(repr(key)) + ", sc: " + str(repr(scancode)) + ", codepoint: " + str(repr(codepoint)) + ", mods: " + str(repr(modifier)))
        if key[1] == "escape":
            keyboard.release()


class KeyboardListener(Widget):
    def __init__(self, kivyroot, **kwargs):
        super(KeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        if self._keyboard.widget:
            # This means we have a vkeyboard object
            pass
        self.handler = InputHandler(kivyroot)
        self._keyboard.bind(on_key_down=self.handler.parse_input)
        Logger.info("Input: Keyboard opened.")

    def keyboard_closed(self):
        Logger.info("Input: Keyboard closed.")
        self._keyboard.unbind(on_key_down=self.handler.parse_input)
        self._keyboard = None
