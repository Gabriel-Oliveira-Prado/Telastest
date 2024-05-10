from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp

class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file("telas\criar_conta\create_account.kv")
    
    def login(self):
        # Atualiza o texto do rótulo acima do cartão com o texto "Bem vindo(a) - nomedapessoa"
        nome_pessoa = self.root.ids.login.text
        self.root.ids.welcome_label.text = f"Bem vindo(a) - {nome_pessoa}"
    
    def on_create_account(self):
        # Carrega a tela de criação de conta
        self.root.current = "criar_conta"  # Navega para a tela de criar conta

if __name__ == "__main__":
    App().run()
