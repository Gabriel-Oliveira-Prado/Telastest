from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
from kivy.metrics import dp
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

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

    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file(os.path.join("menujuridico.kv"))

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
        # Implemente a lógica real do logout aqui
        pass

    def refresh_callback(self):
        # Faça algo quando o layout de atualização for atualizado
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        # Função para trocar de tela
        pass  # Implemente a lógica para trocar de tela aqui

    def show_QuemPoderver(self, button):  # Renomeando o método
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
        # Obter o item selecionado do diálogo
        selected_item = dialog.item.ids.container.text
        # Chamar a função menu_callback com o texto do item selecionado
        self.menu_callback(instance=selected_item)

if __name__ == "__main__":
    App().run()
