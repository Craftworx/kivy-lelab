from kivy.app import App
from kivy.uix.widget import Widget

# structure minimale, on installé les packages et créé une app, ni widget ni layout
# elle tourne mais n'a pas de bouton ni de focntion
class MainWidget(Widget):
    pass

class LelabApp(App):
    pass

LelabApp().run()