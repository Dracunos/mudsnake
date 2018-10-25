from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import common
import outputhandler
import telnethandler

class MainRoot(GridLayout):
    def __init__(self, main_app, **kwargs):
        super(MainRoot, self).__init__(**kwargs)
        self.connection = telnethandler.TelnetHandler("aardwolf.org", 23)
        self.connection.start()
        self.app = main_app
        self.output_handler = outputhandler.OutputHandler()
        def buffer_callback(dx):
            self.ids.outputbuffer.text = self.output_handler.read_to_buffer(self.connection.output_queue)
        Clock.schedule_interval(buffer_callback, 0.05)
        
        
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

            
            
class MudSnakeApp(App):
    def build(self):
       return MainRoot(main_app=self)

if __name__ == '__main__':
    MudSnakeApp().run()
