from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class SelectButtonApp(App):
    def showquem_pode_ver(self,main_button):
        dropdown = DropDown()
        for option in self.quem_pode_ver:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)


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
