from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
import os

class TelaEntrarLogin(Screen):
    pass

class TelaEntrarLoginJuridico(Screen):
    pass

class TelaCriarConta(Screen):
    pass







class App(MDApp):
    def build(self):
        Window.size = (dp(360), dp(640))  # Definindo o tamanho da janela

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        

        # Carregar o arquivo KV que contém a interface do usuário
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    App().run()
