# help_about_screen.py
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# help_and_about_screen.py

# help_about_screen.py

from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.app import MDApp

Builder.load_string("""
<ScreenManagement>:
    HelpAboutScreen:
        name: 'help_about'

<HelpAboutScreen>
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "10dp"
            size_hint_y: None
            height: self.minimum_height
            
            MDLabel:
                text: "How to Use the App"
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
                color:0, 0, 0, 1
            MDLabel:
                text: "1. Capture or upload an image to start."
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "2. The app will process the image and display the result."
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "3. Check the result and explore options like saving or sharing."
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "FAQs"
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "Q1: Why can't I capture a clear image?"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "A1: Make sure the camera lens is clean and try focusing again."
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "Q2: My upload is taking too long. What can I do?"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "A2: Try uploading a smaller image or check your internet connection."
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "About the App"
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "This app helps detect and classify food items using machine learning."
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Version: 1.0.0"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "Developer: Sakhile"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Credits: Kivy, KivyMD, TensorFlow"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "Privacy Policy"
                size_hint_y: None
                height: self.texture_size[1]

            MDRaisedButton:
                text: "Back to Home"
                size_hint: None, None
                size: "200dp", "50dp"
                pos_hint: {"center_x": 0.5}
                on_release: root.go_back()
""")
class HelpAboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_back(self):
        self.manager.current = 'home'


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ScreenManagement(ScreenManager):
    pass
class MyApp(MDApp):
    def build(self):
        # Define the screen manager and load the screen
        screen_manager = ScreenManager()

        # Add screens to the manager
        screen_manager.add_widget(HelpAboutScreen(name='help_about'))
        screen_manager.add_widget(HomeScreen(name='home'))

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
