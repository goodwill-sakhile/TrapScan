import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

class HomeScreen(Screen):
    def go_to_camera(self):
        # Switch to the Camera screen
        self.manager.current = 'camera'

    def go_to_upload(self):
        # Switch to the Image Upload screen
        self.manager.current = 'upload'

    def open_menu(self):
        # Open the menu for History, Settings, and Help options
        self.manager.current = 'menu'


class CameraScreen(Screen):
    def capture_image(self):
        # Logic to capture an image (this is a placeholder for actual camera functionality)
        print("Capturing image...")

    def go_back(self):
        # Go back to Home Screen
        self.manager.current = 'home'


class UploadScreen(Screen):
    def upload_image(self, path):
        # Logic to upload the image (this is a placeholder for actual upload functionality)
        print(f"Uploading image from {path}...")

    def go_back(self):
        # Go back to Home Screen
        self.manager.current = 'home'


class MenuScreen(Screen):
    def go_to_history(self):
        # Navigate to History Screen (this is a placeholder)
        print("Going to History...")

    def go_to_settings(self):
        # Navigate to Settings Screen (this is a placeholder)
        print("Going to Settings...")

    def go_to_help(self):
        # Navigate to Help Screen (this is a placeholder)
        print("Going to Help...")

    def go_back(self):
        # Go back to Home Screen
        self.manager.current = 'home'


class ScreenManagement(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagement:
    HomeScreen:
        name: 'home'
    CameraScreen:
        name: 'camera'
    UploadScreen:
        name: 'upload'
    MenuScreen:
        name: 'menu'

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Home Screen"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Capture Image"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.go_to_camera()
        MDRaisedButton:
            text: "Upload Image"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.go_to_upload()
        MDRaisedButton:
            text: "Menu"
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.open_menu()

<CameraScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Camera Screen"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Capture Image"
            on_release: root.capture_image()
        MDRaisedButton:
            text: "Go Back"
            on_release: root.go_back()

<UploadScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Upload Image"
            halign: 'center'
            font_style: 'H4'
        FileChooserIconView:
            id: filechooser
            on_selection: root.upload_image(filechooser.selection)
        MDRaisedButton:
            text: "Go Back"
            on_release: root.go_back()

<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Menu"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "History"
            on_release: root.go_to_history()
        MDRaisedButton:
            text: "Settings"
            on_release: root.go_to_settings()
        MDRaisedButton:
            text: "Help"
            on_release: root.go_to_help()
        MDRaisedButton:
            text: "Go Back"
            on_release: root.go_back()
""")

if __name__ == '__main__':
    MyApp().run()
