from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
import os

# Importe a classe BoxLayout para construir o ContentNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ContentNavigationDrawer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Adicione widgets ao ContentNavigationDrawer
        button1 = Button(text='Opção 1')
        button2 = Button(text='Opção 2')
        
        self.orientation = 'vertical'
        self.spacing = dp(8)
        
        self.add_widget(button1)
        self.add_widget(button2)

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file(os.path.join("telas\menu\menu.kv"))


if __name__ == "__main__":
    App().run()
