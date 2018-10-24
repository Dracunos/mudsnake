from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import common
import outputhandler
import telnethandler

class Main(GridLayout):
    def __init__(self, main_app, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.connection = telnethandler.TelnetHandler("aardwolf.org", 23)
        self.connection.start()
        self.app = main_app
        self.output_handler = outputhandler.OutputHandler()
        self.cols = 1
        self.exit_button = ExitButton(
            text='exit',
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
            )
        self.output_buffer = OutputBuffer(
            text = "Loading...",
            size_hint = (1, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        self.add_widget(self.exit_button)
        self.add_widget(self.output_buffer)
        def ff(dx):
            self.output_buffer.text = self.output_handler.read_to_buffer(self.connection.output_queue)
        Clock.schedule_interval(ff, 0.2)
        
        
class ExitButton(Label):
    def __init__(self, **kwargs):
        super(ExitButton, self).__init__(**kwargs)
    
    def on_touch_down(self, event):
        if self.collide_point(*event.pos):
            self.parent.app.stop()
            return True
        else:
            return super(ExitButton, self).on_touch_down(event)

class OutputBuffer(Label):
    def __init__(self, **kwargs):
        super(OutputBuffer, self).__init__(**kwargs)

            
            
class MudApp(App):
    def build(self):
        self.root = root = Main(main_app=self)
        return root
        

if __name__ == '__main__':
    MudApp().run()