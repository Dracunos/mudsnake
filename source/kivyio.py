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
        self.connection = telnethandler.TelnetHandler("aardwolf.org", 23, self.buffer_callback)
        self.connection.start()
        self.app = main_app
        self.output_handler = outputhandler.OutputHandler()
        #Clock.schedule_interval(self.buffer_callback, 0.05)
        
    def buffer_callback(self):
        self.ids.outputbuffer.text = self.output_handler.read_to_buffer(self.connection.output_queue)
        self.ids.outputbuffer.scroll_to_bottom()
        
        
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
