from kivy.config import Config
Config.set("kivy", "exit_on_escape", "0")
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import common
import outputhandler
import telnethandler

class MainRoot(GridLayout):
    def __init__(self, main_app, **kwargs):
        super(MainRoot, self).__init__(**kwargs)
        self.connection = telnethandler.TelnetHandler(
            "aardwolf.org", 23, self.buffer_callback)
        self.connection.start()
        self.app = main_app
        self.output_handler = outputhandler.OutputHandler()
        self.ids.inputbox.bind(on_text_validate=self.text_input_callback)
        
    def buffer_callback(self):
        mybuffer = self.ids.outputbuffer
        mybuffer.text = self.output_handler.read_to_buffer(
            self.connection.output_queue)
        mybuffer.scroll_to_bottom()

    def text_input_callback(self, text):
        self.connection.send(text)
        Clock.schedule_once(self.focus_text_box)
    
    def focus_text_box(self, *args):
        self.ids.inputbox.focus = True
        
        
class ExitButton(Label):
    def __init__(self, **kwargs):
        super(ExitButton, self).__init__(**kwargs)
    
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

            
            
class MudSnakeApp(App):
    def build(self):
       return MainRoot(main_app=self)

if __name__ == '__main__':
    MudSnakeApp().run()
