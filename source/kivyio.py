from kivy.config import Config
Config.set("kivy", "exit_on_escape", "0")
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import common
import outputhandler
import inputhandler
import telnethandler

class MainRoot(GridLayout):
    def __init__(self, main_app, **kwargs):
        super(MainRoot, self).__init__(**kwargs)
        self.connection = telnethandler.TelnetHandler(
            "aardwolf.org", 23, self.buffer_callback)
        self.connection.start()
        self.app = main_app
        self.ids.kbbutt.bind(on_touch_down = self.kbbuttonpress)
        self.input_handler = inputhandler.InputHandler(self)
        Window.bind(on_keyboard = self.input_handler.parse_input)
        self.output_handler = outputhandler.OutputHandler()
        Clock.schedule_interval(self.constant_callback, 0.05)
        
    def kbbuttonpress(self, *args):
        Window.request_keyboard(self.resize_screen, self)
    
    def constant_callback(self, dt=0):
        self.resize_screen()
        self.ids.outputbuffer.scroll_to_bottom()
        
    def resize_screen(self):
        kb_size = Window.keyboard_height
        self.ids.kboffset.height = kb_size
        
    def buffer_callback(self):
        mybuffer = self.ids.outputbuffer
        mybuffer.text = self.output_handler.read_to_buffer(
            self.connection.output_queue)
        mybuffer.scroll_to_bottom()
   
        
class ExitButton(Label):
    
    def on_touch_down(self, event):
        if self.collide_point(*event.pos):
            self.parent.connection.end()
            self.parent.app.stop()
            return True
        else:
            return super(ExitButton, self).on_touch_down(event)

class OutputBuffer(Label):
    def __init__(self, **kwargs):
        super(OutputBuffer, self).__init__(**kwargs)
        
    def scroll_to_bottom(self):
       self.parent.scroll_to(self)
       
       
class InputBox(TextInput):
    pass
    
class KeyboardOffset(Label):
    pass

            
            
class MudSnakeApp(App):
    def build(self):
       return MainRoot(main_app=self)

if __name__ == '__main__':
    MudSnakeApp().run()
