from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os

# Load the .kv UI design file
Builder.load_file("gui/ui.kv")  # adjust if path differs

class AssistantLayout(BoxLayout):
    def activate_assistant(self):
        os.system('start "" cmd /k "cd /d ../assistant && venv\\Scripts\\activate && python main.py"')

class AssistantApp(App):
    def build(self):
        return AssistantLayout()

if __name__ == '__main__':
    AssistantApp().run()
