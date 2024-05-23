from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class SelectButtonApp(App):
    def build(self):
        main_button = Button(text='Selecionar Opções', size_hint=(None, None), size=(200, 50))
        dropdown = DropDown()

        # Adiciona algumas opções ao dropdown
        for option in ['Opção 1', 'Opção 2', 'Opção 3']:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Abre o dropdown quando o botão principal é clicado
        main_button.bind(on_release=dropdown.open)

        # Atualiza o texto do botão principal com a opção selecionada
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        return main_button


if __name__ == '__main__':
    SelectButtonApp().run()
