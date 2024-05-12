from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.lang import Builder
Window.size = (300, 500)


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


KV = '''
<ContentNavigationDrawer>:
    orientation: 'vertical'
    spacing: dp(8)
    
    MDLabel:
        text: 'Meu Drawer'
        font_style: 'Subtitle1'
        size_hint_y: None
        height: self.texture_size[1]

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(4)

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(4)
        MDIconButton:
            icon: "cog"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # cor branca
            text: 'Configurações'
            on_release: app.change_screen('configuracoes')  
        MDLabel:
            text: 'Configurações'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # cor branca
            halign: 'left'
            font_style: 'Subtitle2'
            size_hint_y: None
            height: self.texture_size[1]

MDScreen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#ffffff"  # Cor de fundo branca
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
                
                MDBottomNavigation:
                    background_color: 1, 1, 1, 1  # Cor de fundo branca
                    #panel_color: "#eeeaea"
                    selected_color_background: "purple"
                    text_color_active: "lightgrey"

                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Menu'
                        icon: 'home'

                        MDLabel:
                            text: 'Menu'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'Pesquisar'
                        icon: 'magnify'

                        MDLabel:
                            text: 'Pesquisar'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 3'
                        text: 'Notificações'
                        icon: 'bell-ring'

                        MDLabel:
                            text: 'notificações'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 4'
                        text: 'Publicações'
                        icon: 'plus-box-multiple'

                        MDLabel:
                            text: 'Publicaçõess'
                            halign: 'center'
                        
        MDNavigationDrawer:
            id: nav_drawer
            spacing: 10
            radius: (0, 16, 16, 0)
            background_color: 1, 1, 1, 1  # Cor de fundo branca
        
            MDIconButton:
                icon: "account-circle"
                text: 'Conta'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # cor branca
                on_release: app.change_screen('Conta')  

            MDIconButton:
                icon: "cog"
                text: 'configuracoes'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # cor branca
                on_release: app.change_screen('configuracoes')  
'''


class ContentNavigationDrawer(MDBoxLayout):
    pass


MainApp().run()
