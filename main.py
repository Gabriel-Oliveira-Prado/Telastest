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
        'Criar Grupo': 'account-multiple-outline',
        'Criar Comunidade': 'account-group-outline',
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

    def show_QuemPoderver(self, button):  
        dialog = MDDialog(
            title="Quem pode ver:",
            type="confirmation",
            items=[
                ItemConfirm(text="Todos"),
                ItemConfirm(text="Apenas Conexões"),
            ],
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda *args: dialog.dismiss()
                ),
                MDFlatButton(
                    text="Confirmar",
                    on_release=lambda *args: self.confirm_action(dialog)
                )
            ]
        )
        dialog.open()

    def menu_callback(self, instance):
        Snackbar(text=instance.text).open()

    def confirm_action(self, dialog):
        selected_item = dialog.item.ids.container.text
        self.menu_callback(instance=selected_item)

if __name__ == "__main__":
    App().run()