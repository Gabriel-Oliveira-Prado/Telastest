from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem
import os
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField

class ConfigItem(OneLineIconListItem):
    pass

class LimitedMDTextField(MDTextField):
    max_text_length = 500
    def insert_text(self, substring, from_undo=False):
        if len(self.text) + len(substring) > self.max_text_length:
            substring = substring[:self.max_text_length - len(self.text)]
        return super().insert_text(substring, from_undo=from_undo)

class App(MDApp):
    def build(self):
        
        Window.size = (dp(360), dp(640))
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Purple"
        return Builder.load_file(os.path.join("telas\config_Perfil\config_Perfil.kv"))

    def show_logout_dialog(self):
        dialog = MDDialog(
            text="Deseja sair da conta?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="Sim",
                    on_release=lambda *args: self.logout()
                )
            ]
        )
        dialog.open()

    def logout(self):
       
        pass

    def switch_screen(self, screen_name):
        
        pass  

    def limitar_caracteres(self, widget, text):
        if len(text) > widget.max_text_length:
            widget.text = text[:widget.max_text_length]

if __name__ == "__main__":
    App().run()
