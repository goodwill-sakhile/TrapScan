# main.py
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView


class HomeScreen(Screen):
    def go_to_camera(self):
        self.manager.current = 'camera'

    def go_to_upload(self):
        self.manager.current = 'upload'

    def open_menu(self):
        self.manager.current = 'menu'


class ProcessingScreen(Screen):
    def process_image(self, image_path):
        print(f"Processing the image at {image_path}...")

    def go_back(self):
        self.manager.current = 'home'


class UploadScreen(Screen):
    def upload_image(self, path):
        print(f"Image selected: {path[0]}")

    def proceed_to_processing(self, path):
        if path:
            self.manager.current = 'processing'
            self.manager.get_screen('processing').process_image(path[0])

    def go_back(self):
        self.manager.current = 'home'


class ResultScreen(Screen):
    def show_details(self):
        # Navigate to the More Info screen
        self.manager.current = 'more_info'

    def go_back(self):
        self.manager.current = 'home'


class MoreInfoScreen(Screen):
    def view_details(self):
        # This could be a placeholder for displaying more detailed information.
        print("Displaying more details...")

    def back_to_result(self):
        self.manager.current = 'result'

    def go_home(self):
        self.manager.current = 'home'


class MenuScreen(Screen):
    def go_to_history(self):
        print("Going to History...")

    def go_to_settings(self):
        print("Going to Settings...")

    def go_to_help(self):
        print("Going to Help...")

    def go_back(self):
        self.manager.current = 'home'


class ScreenManagement(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        return Builder.load_string("""
ScreenManagement:
    HomeScreen:
        name: 'home'
    ProcessingScreen:
        name: 'processing'
    UploadScreen:
        name: 'upload'
    ResultScreen:
        name: 'result'
    MoreInfoScreen:
        name: 'more_info'
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

<ProcessingScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Processing Image"
            halign: 'center'
            font_style: 'H4'
        MDLabel:
            text: "The image is being processed..."
            halign: 'center'
            font_style: 'Body1'
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
            text: "Proceed"
            on_release: root.proceed_to_processing(filechooser.selection)
        MDRaisedButton:
            text: "Go Back"
            on_release: root.go_back()

<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Result Screen"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "View Details"
            on_release: root.show_details()
        MDRaisedButton:
            text: "Go Back"
            on_release: root.go_back()

<MoreInfoScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "More Information"
            halign: 'center'
            font_style: 'H4'
        MDLabel:
            text: "Detailed information about the result is displayed here."
            halign: 'center'
            font_style: 'Body1'
        MDRaisedButton:
            text: "Back to Result"
            on_release: root.back_to_result()
        MDRaisedButton:
            text: "Go Home"
            on_release: root.go_home()

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
