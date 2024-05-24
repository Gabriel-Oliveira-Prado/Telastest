from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class App(MDApp):
    def build(self):
        # Definindo a resolução da janela para um tamanho típico de tela de celular
        Window.size = (dp(360), dp(640))  # Largura x Altura em dp

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"

        # Defina as opções
        self.especificacao = [
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
        self.cargo = [
            'Operacionais e de Suporte',
            'Técnico e Especializado',
            'Supervisão e Coordenação',
            'Gerência',
            'Chefia e Direção',
            'Executivos'
        ]
        self.local_de_trabalho = [
            'Presencial',
            'Híbrido',
            'Remoto'
        ]
        self.localidade  = [
            'AL - Arapiraca',
            'AL - Campo Alegre',
            'AL - Coruripe',
            'AL - Delmiro Gouveia',
            'AL - Maceió',
            'AL - Palmeira dos Índios',
            'AL - Penedo',
            'AL - Rio Largo',
            'AL - São Miguel dos Campos',
            'AL - União dos Palmares',
            'BA - Camaçari',
            'BA - Feira de Santana',
            'BA - Ilhéus',
            'BA - Itabuna',
            'BA - Jequié',
            'BA - Juazeiro',
            'BA - Lauro de Freitas',
            'BA - Salvador',
            'BA - Teixeira de Freitas',
            'BA - Vitória da Conquista',
            'CE - Caucaia',
            'CE - Crato',
            'CE - Fortaleza',
            'CE - Iguatu',
            'CE - Itapipoca',
            'CE - Juazeiro do Norte',
            'CE - Maracanaú',
            'CE - Maranguape',
            'CE - Quixadá',
            'CE - Sobral',
            'MA - Açailândia',
            'MA - Bacabal',
            'MA - Caxias',
            'MA - Codó',
            'MA - Imperatriz',
            'MA - Paço do Lumiar',
            'MA - Pinheiro',
            'MA - Santa Inês',
            'MA - São Luís',
            'MA - Timon',
            'PB - Bayeux',
            'PB - Cabedelo',
            'PB - Cajazeiras',
            'PB - Campina Grande',
            'PB - Guarabira',
            'PB - João Pessoa',
            'PB - Patos',
            'PB - Pombal',
            'PB - Santa Rita',
            'PB - Sousa',
            'PE - Cabo de Santo Agostinho',
            'PE - Camaragibe',
            'PE - Caruaru',
            'PE - Garanhuns',
            'PE - Jaboatão dos Guararapes',
            'PE - Olinda',
            'PE - Paulista',
            'PE - Petrolina',
            'PE - Recife',
            'PE - Vitória de Santo Antão',
            'PI - Altos',
            'PI - Barras',
            'PI - Campo Maior',
            'PI - Floriano',
            'PI - José de Freitas',
            'PI - Parnaíba',
            'PI - Picos',
            'PI - Piripiri',
            'PI - Teresina',
            'PI - União',
            'RN - Apodi',
            'RN - Caicó',
            'RN - Ceará-Mirim',
            'RN - Currais Novos',
            'RN - Macaíba',
            'RN - Mossoró',
            'RN - Natal',
            'RN - Parnamirim',
            'RN - Santa Cruz',
            'RN - São Gonçalo do Amarante',
            'SE - Aracaju',
            'SE - Estância',
            'SE - Itabaiana',
            'SE - Itaporanga DAjuda',
            'SE - Lagarto',
            'SE - Nossa Senhora do Socorro',
            'SE - Propriá',
            'SE - São Cristóvão',
            'SE - Simão Dias',
            'SE - Tobias Barreto'
        ]
        self.tipo_de_vaga = [
            'Tempo integral',
            'Meio período',
            'Contrato',
            'Temporário',
            'Outro',
            'Voluntário',
            'Estágio'
        ]

        # Cria a interface usando o arquivo KV
        return Builder.load_file("criarvaga.kv")

    def show_especificacao(self, main_button):
        dropdown = DropDown()
        for option in self.especificacao:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_cargo(self, main_button):
        dropdown = DropDown()
        for option in self.cargo:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_local_de_trabalho(self, main_button):
        dropdown = DropDown()
        for option in self.local_de_trabalho:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_localidade(self, main_button):
        dropdown = DropDown()
        for option in self.localidade:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)
    
    def show_tipo_de_vaga(self, main_button):
        dropdown = DropDown()
        for option in self.tipo_de_vaga:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def select_option(self, dropdown, text, main_button):
        main_button.text = text
        dropdown.dismiss()
        # Mantendo a largura fixa
        main_button.size_hint_x = None
        main_button.width = dp(200)

if __name__ == "__main__":
    App().run()
