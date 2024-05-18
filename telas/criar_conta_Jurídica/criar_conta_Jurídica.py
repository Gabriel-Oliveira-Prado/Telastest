from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu


from kivy.metrics import dp

class App(MDApp):
    def build(self):
        
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file("telas\criar_conta_Jurídica\criar_conta_Jurídica.kv")
    
    def login(self):
        # Atualiza o texto do rótulo acima do cartão com o texto "Bem vindo(a) - nomedapessoa"
        nome_pessoa = self.root.ids.login.text
        self.root.ids.welcome_label.text = f"Bem vindo(a) - {nome_pessoa}"
        
    
    def format_date(self, text):
        # Remove todos os caracteres que não são dígitos
        text = ''.join(c for c in text if c.isdigit())

        # Insere barras após o segundo e quinto caractere
        if len(text) >= 2 and text[1] != '/':
            text = text[:2] + '/' + text[2:]
        if len(text) >= 5 and text[4] != '/':
            text = text[:5] + '/' + text[5:]

        # Limita o dia entre 01 e 31
        day = text[:2]
        if day and not 1 <= int(day) <= 31:
            text = text[:1]

        # Limita o mês entre 01 e 12
        month = text[3:5]
        if month and not 1 <= int(month) <= 12:
            text = text[:4]

        # Limita o ano entre 1900 e 9999
        year = text[6:10]
        if year and not 1900 <= int(year) <= 2024:
            text = text[:6]

        return text[:10]  # Garante que o texto tenha no máximo 10 caracteres
if __name__ == "__main__":
    App().run()
