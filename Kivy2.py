from kivy.app import App
from kivy.app import Widget

class HellowWorld(App):
    def build(self):
        self.root = Widget()
        return self.root

HellowWorld().run()