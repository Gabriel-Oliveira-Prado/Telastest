from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import os

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"

        # Defina as opções
        self.options1 = [
            'Administração e Escritório',
            'Tecnologia da Informação',
            'Marketing e Vendas',
            'Recursos Humanos',
            'Finanças',
            'Engenharia',
            'Saúde',
            'Educação',
            'Design e Criação',
            'Logística e Transporte',
            'Jurídico',
            'Atendimento ao Cliente',
            'Operações e Produção',
            'Cargos de Nível Executivo'
        ]
        self.options2 = [
            'Operacionais e de Suporte'
            'Técnico e Especializado'
            'Supervisão e Coordenação'
            'Gerência'
            'Chefia e Direção'
            'Executivos'
        ]

        return Builder.load_file(os.path.join("criarvaga.kv"))

    
    def show_options1   (self, main_button):
        dropdown = DropDown()
        for option in self.options1:
            btn = Button(text=option, size_hint_y=None, height=dp(44),width=dp(44))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn.background_color = (0, 0, 0, 0) 
            btn.color = (0, 0, 0, 1)  
            dropdown.add_widget(btn)
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
    def show_options2   (self, main_button):
        dropdown = DropDown()
        for option in self.options2:
            btn = Button(text=option, size_hint_y=None, height=dp(44),width=dp(44))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn.background_color = (0, 0, 0, 0) 
            btn.color = (0, 0, 0, 1)  
            dropdown.add_widget(btn)
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
if __name__ == "__main__":
    App().run()
