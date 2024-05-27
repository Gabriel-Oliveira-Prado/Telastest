from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
import os
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.switch import Switch
import sqlite3

class TelaEntrarLogin(Screen):
    pass

class TelaEntrarLoginJuridico(Screen):
    pass

class TelaCriarConta(Screen):
    pass

class TelaCriarContaJuridico(Screen):
    pass

class TelaMenu(Screen):
    pass

class Telaconfignotificacoes(Screen):
    pass

class TelaconfigPrivacidadeDados(Screen):
    pass

class TelaconfigVisibilidade(Screen):
    pass

class TelaconfigSeguranca(Screen):
    pass

class TelaconfigPerfil(Screen):
    pass

class TelaSalvos(Screen):
    pass

class Telanotificacoes(Screen):
    pass

class TelaChat(Screen):
    pass

class TelaPublicacoes(Screen):
    pass

class TelaInformacoesPerfil(Screen):
    pass

class TelaEnderecoemail(Screen):
    pass

class TelaTrocarSenha(Screen):
    pass

class Telanumerostelefone(Screen):
    pass

class ItemConfirm(OneLineIconListItem):
    pass

class ConfigItem(OneLineIconListItem):
    pass

class LimitedMDTextField(MDTextField):
    max_text_length = 500
    def insert_text(self, substring, from_undo=False):
        if len(self.text) + len(substring) > self.max_text_length:
            substring = substring[:self.max_text_length - len(self.text)]
        return super().insert_text(substring, from_undo=from_undo)

class App(MDApp):
    dialog = None

    data = {
        'Bloquear': 'block-helper',
    }

    def build(self):
        Window.size = (dp(360), dp(640))  
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file(os.path.join("main.kv"))

    def show_logout_dialog(self):
        self.dialog = MDDialog(
            text="Deseja sair da conta?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda *args: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Sim",
                    on_release=lambda *args: self.logout_and_dismiss()
                )
            ]
        )
        self.dialog.open()

    def logout_and_dismiss(self):
        self.dialog.dismiss() 
        self.logout() 

    def logout(self):
        self.root.current = 'Entrar_login'

    def refresh_callback(self):
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        pass

    def showquem_pode_ver(self, main_button):
        self.quem_pode_ver = ['            Todos            ', 'Apenas Empresas']  
        dropdown = DropDown()
        for option in self.quem_pode_ver:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (1, 1, 1, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def menu_callback(self, instance):
        Snackbar(text=instance.text).open()

    def confirm_action(self, dialog):
        selected_item = dialog.item.ids.container.text
        self.menu_callback(instance=selected_item)

    def select_option(self, dropdown, text, main_button):
        main_button.text = text
        dropdown.dismiss()
        main_button.size_hint_x = None
        main_button.width = dp(150)

if __name__ == "__main__":
    App().run()