from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

# Declare both screens
class LoginScreen(Screen):
    pass
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_fucking_press(self):
        print('You press me')
class LoginWidget(BoxLayout):
    pass
class PasswordWidget(BoxLayout):
    pass
class SettingsScreen(Screen):
    pass
class ScreenManagerApp(ScreenManager):
    pass
kv=Builder.load_file("my.kv")
class TestApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    TestApp().run()
