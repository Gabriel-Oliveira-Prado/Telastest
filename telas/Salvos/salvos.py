from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
import os
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton



class ConfigItem(OneLineIconListItem):
    pass

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Purple"
        return Builder.load_file(os.path.join("telas\Salvos\salvos.kv"))
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


if __name__ == "__main__":
    App().run()
