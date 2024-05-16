from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

# Carregando os arquivos kv
Builder.load_file('tela1.kv')
Builder.load_file('tela2.kv')

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        # Criando um gerenciador de tela
        sm = ScreenManager()
        # Adicionando as telas ao gerenciador de tela
        sm.add_widget(Screen1(name='tela1'))
        sm.add_widget(Screen2(name='tela2'))
        return sm

if __name__ == '__main__':
    TestApp().run()
