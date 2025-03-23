# settings_screen.py
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.switch import MDSwitch
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dropdownmenu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change_theme(self, instance, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def change_language(self, instance, value):
        # Placeholder for language change
        print(f"Language changed to: {value}")

    def clear_cache(self):
        # Placeholder for clearing cache functionality
        print("Cache cleared")

    def go_back(self):
        self.manager.current = 'home'


class MyApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagement:
    SettingsScreen:
        name: 'settings'

<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Settings"
            halign: 'center'
            font_style: 'H4'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "48dp"
            MDLabel:
                text: "Dark Theme"
            MDSwitch:
                on_active: root.change_theme(*args)
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "48dp"
            MDLabel:
                text: "Language"
            MDDropdownMenu:
                items: ['English', 'Spanish', 'French']
                on_select: root.change_language(*args)
        MDRaisedButton:
            text: "Clear Cache"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.clear_cache()
        MDRaisedButton:
            text: "Go Back"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.go_back()
""")

if __name__ == '__main__':
    MyApp().run()
