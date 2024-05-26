import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp  # Importe MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

kivy.require('1.2.0')  # Substitua pela versão do Kivy que você usa

Builder.load_string('''
<TelaPrincipal>:
    name: 'principal'
    MDLabel:
        text: root.texto_publicado
        halign: 'center'
        font_style: 'H3'

<TelaPublicacao>:
    name: 'publicacao'
    MDLabel:
        text: 'Digite o texto a ser publicado:'
        halign: 'center'
    MDTextField:
        id: texto_input
        hint_text: 'Texto aqui...'
        multiline: True
        size_hint_y: None
        height: '100dp'
    MDRaisedButton:
        text: 'Publicar'
        on_press: root.publicar()
''')

class TelaPrincipal(Screen):
    texto_publicado = StringProperty('')

class TelaPublicacao(Screen):
    def publicar(self):
        texto = self.ids.texto_input.text
        self.manager.get_screen('principal').texto_publicado = texto
        self.manager.current = 'principal'

class MyApp(MDApp):  # Herde de MDApp
    theme_cls = ThemeManager()
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaPrincipal())
        sm.add_widget(TelaPublicacao())
        return sm

if __name__ == '__main__':
    MyApp().run()