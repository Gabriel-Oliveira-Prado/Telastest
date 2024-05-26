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
import sqlite3

class TelaEntrarLogin(Screen):
    def login(self):
        usuario = self.ids.login.text
        senha = self.ids.senha.text

        # Conexão com o banco de dados 
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Verifique se a tabela existe, se não, crie-a
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                usuario TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                telefone TEXT,  -- Adicionado campo telefone para usuários jurídicos
                tipo TEXT NOT NULL DEFAULT 'fisica' 
            )
        """)

        cursor.execute(
            """SELECT * FROM usuarios WHERE usuario = ? AND senha = ? AND tipo = 'fisica'""",
            (usuario, senha),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            # Login bem-sucedido
            self.parent.current = 'Menu'
            self.parent.get_screen('Menu').ids.Username.text = user[1]
        else:
            Snackbar(text="Usuário ou senha incorretos!").open()

class TelaEntrarLoginJuridico(Screen):
    def login_juridico(self):
        cnpj = self.ids.login.text
        senha = self.ids.senha.text

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM usuarios WHERE usuario = ? AND senha = ? AND tipo = 'juridica'""",
            (cnpj, senha),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            self.parent.current = 'Menu'
            self.parent.get_screen('Menu').ids.Username.text = user[1]
        else:
            Snackbar(text="CNPJ ou senha incorretos!").open()

class TelaCriarConta(Screen):
    def cadastrar(self):
        nome = self.ids.nome.text
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        confirmar_senha = self.ids.confirmar_senha.text

        if senha != confirmar_senha:
            Snackbar(text="As senhas não coincidem!").open()
            return

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, usuario, senha)
                VALUES (?, ?, ?)
                """,
                (nome, usuario, senha),
            )
            conn.commit()
            Snackbar(text="Usuário cadastrado com sucesso!").open()
            self.parent.current = 'Entrar_login' 
        except sqlite3.IntegrityError:
            Snackbar(text="Este nome de usuário já está em uso.").open()
        finally:
            conn.close()

class TelaCriarContaJuridico(Screen):
    def cadastrar_juridico(self):
        nome_empresa = self.ids.nome_empresa.text
        cnpj = self.ids.cnpj.text
        senha = self.ids.senha.text
        telefone = self.ids.telefone.text

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, usuario, senha, telefone, tipo)
                VALUES (?, ?, ?, ?, 'juridica')
                """,
                (nome_empresa, cnpj, senha, telefone), 
            )
            conn.commit()
            Snackbar(text="Usuário jurídico cadastrado com sucesso!").open()
            self.parent.current = 'Entrar_login'  
        except sqlite3.IntegrityError:
            Snackbar(text="Este CNPJ já está em uso.").open()
        finally:
            conn.close()

class TelaMenu(Screen):
    pass

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

class TelaPublicacoes(Screen):
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