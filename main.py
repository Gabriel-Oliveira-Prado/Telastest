from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
import os
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivymd.uix.card import MDCard
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA3gOHi9Q6aHQ5seN5S9bbNmQpPQFMGXFs",
    'authDomain': "magnus-c4b38.firebaseapp.com",
    'databaseURL': "https://magnus-c4b38-default-rtdb.firebaseio.com",
    'projectId': "magnus-c4b38",
    'storageBucket': "magnus-c4b38.appspot.com",
    'messagingSenderId': "458576341456",
    'appId': "1:458576341456:web:6117f4a9160b8667b8f1d5"
}


class TelaEntrarLogin(Screen):
    def Login(self):
        email = self.ids.email.text
        senha = self.ids.senha.text
        
        if not email or not senha:
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email, senha)
            print("Login realizado com sucesso.")
            # Navegar para outra tela após login bem-sucedido
            self.manager.current = 'Menu'
        except Exception as e:
            print("Erro ao fazer login:", e)

class TelaEntrarLoginJuridico(Screen):
     def LoginJuridico(self):
        cnpj = self.ids.cnpj.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        
        if not all([cnpj, email, senha]):
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email, senha)
            print("Login realizado com sucesso.")
            # Navegar para outra tela após login bem-sucedido
            self.manager.current = 'Menu'
        except Exception as e:
            print("Erro ao fazer login:", e)

class TelaCriarConta(Screen):
    def Cadastra(self):
        nome = self.ids.nome.text
        nome_social = self.ids.nome_social.text
        cpf = self.ids.cpf.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        confirmar_senha = self.ids.confirmar_senha.text
        data_nascimento = self.ids.data_nascimento.text
        
        if not all([nome, cpf, email, senha, confirmar_senha, data_nascimento]):
            print("Por favor, preencha todos os campos.")
            return
        
        if senha != confirmar_senha:
            print("As senhas não coincidem.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.create_user_with_email_and_password(email, senha)
            db = firebase.database()
            data = {
                "nome": nome,
                "nome_social": nome_social,
                "cpf": cpf,
                "email": email,
                "data_nascimento": data_nascimento
            }
            db.child("users").child(user["localId"]).set(data)
            print("Usuário registrado com sucesso.")
        except Exception as e:
            print("Erro ao registrar o usuário:", e)

class TelaCriarContaJuridico(Screen):
     def CadastrarJuridico(self):
        nome_empresa = self.ids.nome_empresa.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        telefone = self.ids.telefone.text
        cnpj = self.ids.cnpj.text
        
        if not all([nome_empresa, email, senha, telefone, cnpj]):
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.create_user_with_email_and_password(email, senha)
            db = firebase.database()
            data = {
                "nome_empresa": nome_empresa,
                "email": email,
                "telefone": telefone,
                "cnpj": cnpj
            }
            db.child("users_juridicos").child(user["localId"]).set(data)
            print("Conta jurídica registrada com sucesso.")
        except Exception as e:
            print("Erro ao registrar a conta jurídica:", e)

class TelaMenu(Screen):
    def update_publicacoes(self, texto):
        box = self.ids.box
        num_linhas = texto.count('\n') + 1  # Conta o número de quebras de linha e adiciona 1 para a última linha
        altura_card = str(num_linhas * 20 + 40) + 'dp'  # Ajusta a altura do card com base no número de linhas
        new_card = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            size=("280dp", altura_card),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            elevation=1,  # Define a elevação como 1
            padding="10dp",
        )
        new_label = MDLabel(
            text=texto,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            halign="left",
            size_hint_y=None,
            height="40dp"
        )
        new_card.add_widget(new_label)
        box.add_widget(new_card)


class TelaPublicacoes(Screen):
     def publicar(self):
        texto = self.ids.publicacao_text.text
        if texto:
            app = MDApp.get_running_app()
            menu_screen = app.root.get_screen('Menu')
            menu_screen.update_publicacoes(texto)
            self.ids.publicacao_text.text = ""
            app.root.transition.direction = 'right'
            app.root.current = 'Menu'

class Telaconfignotificacoes(Screen):
    pass

class TelaconfigPrivacidadeDados(Screen):
    pass

class TelaconfigVisibilidade(Screen):
    pass

class TelaconfigSeguranca(Screen):
    pass

class TelaconfigPerfil(Screen):
    pass

class TelaSalvos(Screen):
    pass

class Telanotificacoes(Screen):
    pass

class TelaChat(Screen):
    pass

class TelaInformacoesPerfil(Screen):
    pass

class TelaEnderecoemail(Screen):
    pass

class TelaTrocarSenha(Screen):
    pass

class Telanumerostelefone(Screen):
    pass

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

    data = {
        'Bloquear': 'block-helper',
    }

    def build(self):
        Window.size = (dp(360), dp(640))  
        Window.clearcolor = (1, 1, 1, 1)

        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file(os.path.join("main.kv"))

    def show_logout_dialog(self):
        self.dialog = MDDialog(
            text="Deseja sair da conta?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda *args: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Sim",
                    on_release=lambda *args: self.logout_and_dismiss()
                )
            ]
        )
        self.dialog.open()

    def logout_and_dismiss(self):
        self.dialog.dismiss() 
        self.logout() 

    def logout(self):
        self.root.current = 'Entrar_login'

    def refresh_callback(self):
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        pass

    def showquem_pode_ver(self, main_button):
        self.quem_pode_ver = ['            Todos            ', 'Apenas Empresas']  
        dropdown = DropDown()
        for option in self.quem_pode_ver:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (1, 1, 1, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def menu_callback(self, instance):
        Snackbar(text=instance.text).open()

    def confirm_action(self, dialog):
        selected_item = dialog.item.ids.container.text
        self.menu_callback(instance=selected_item)

    def select_option(self, dropdown, text, main_button):
        main_button.text = text
        dropdown.dismiss()
        main_button.size_hint_x = None
        main_button.width = dp(150)

if __name__ == "__main__":
    App().run()