from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.widget import Widget

class InputHandler(object):
    def __init__(self, inputbox):
        self.inputbox = inputbox
    
    def parse_input(self, s):
        Logger.info("Input: " + str(repr(s)))
        if s == "\n":
            self.inputbox.root.connection.send(self.inputbox.text)
            self.inputbox.text = ""
            return ""
        return s
