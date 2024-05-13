from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
import os
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class RefreshLayoutContent(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Adicione widgets ao RefreshLayoutContent
        self.layout = MDGridLayout(cols=1, adaptive_height=True, spacing=dp(10))
        for i in range(10):
            btn = Button(text=f'Item {i}')
            self.layout.add_widget(btn)
        
        self.add_widget(self.layout)

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Purple"
        return Builder.load_file(os.path.join("telas\menu\menu.kv"))

    def refresh_callback(self):
        # Faça algo quando o layout de atualização for atualizado
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        # Função para trocar de tela
        pass  # Implemente a lógica para trocar de tela aqui

if __name__ == "__main__":
    App().run()
