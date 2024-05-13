from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton

KV = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        size_hint_y: None
        height: dp(56)
        padding: dp(8)

        MDIconButton:
            icon: "menu"
            on_release: app.callback()

        Widget:

        MDIconButton:
            icon: "magnify"
            on_release: app.toggle_search()

    ScrollView:

        # Conteúdo da aplicação aqui
'''


class SearchApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        self.search_field = MDTextField(
            hint_text="Pesquisar",
            size_hint_x=None,
            width=200,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            mode="rectangle"
        )
        return self.root

    def toggle_search(self):
        if self.search_field.parent:
            self.root.remove_widget(self.search_field)
        else:
            self.root.add_widget(self.search_field)

    def callback(self):
        print("Menu clicado!")


SearchApp().run()
