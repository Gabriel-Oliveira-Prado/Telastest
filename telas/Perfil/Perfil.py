from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem
import os

# Importando a classe `ScrollView` e `LimitedMDTextField` do KivyMD
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField

class ConfigItem(OneLineIconListItem):
    pass

class LimitedMDTextField(MDTextField):
    max_text_length = 500
    
    def insert_text(self, substring, from_undo=False):
        # Verifica se o comprimento total do texto excede o limite
        if len(self.text) + len(substring) > self.max_text_length:
            # Trunca a substring para garantir que o comprimento total não exceda o limite
            substring = substring[:self.max_text_length - len(self.text)]
        # Insere o texto limitado
        return super().insert_text(substring, from_undo=from_undo)

# Restante do seu código permanece o mesmo

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Purple"
        return Builder.load_file(os.path.join("telas\Perfil\Perfil.kv"))

    def switch_screen(self, screen_name):
        # Função para trocar de tela
        pass  # Implemente a lógica para trocar de tela aqui

    def limitar_caracteres(self, widget, text):
        if len(text) > widget.max_text_length:
            widget.text = text[:widget.max_text_length]

if __name__ == "__main__":
    App().run()
