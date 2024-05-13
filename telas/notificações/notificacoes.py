from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.metrics import dp
import os

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp

        self.theme_cls.primary_palette = "Purple"
        return Builder.load_file(os.path.join("telas", "notificações", "notificacoes.kv"))

    
    def refresh_callback(self):
        # Faça algo quando o layout de atualização for atualizado
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        # Função para trocar de tela
        pass  # Implemente a lógica para trocar de tela aqui


if __name__ == "__main__":
    App().run()
