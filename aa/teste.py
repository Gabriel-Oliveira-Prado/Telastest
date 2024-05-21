from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.screenmanager import ScreenManager, Screen

class MainApp(MDApp):
    def build(self):
        self.layout = MDBoxLayout(orientation="vertical")

        button = MDRaisedButton(
            text="Abrir Bottom Sheet",
            pos_hint={"center_x": .5, "center_y": .5},
            on_release=self.show_grid_bottom_sheet
        )

        self.layout.add_widget(button)
        
        # Crie o BottomSheet aqui e adicione ao layout
        self.bottom_sheet_menu = MDGridBottomSheet()
        self.layout.add_widget(self.bottom_sheet_menu)
        
        return self.layout

    def show_grid_bottom_sheet(self, instance):
        # Definindo um layout de grade para os itens
        grid_layout = MDGridLayout(cols=2)  # 2 colunas
        
        for item in menu_items:
            # Criando o widget do item
            button = MDRaisedButton(**item)  
            grid_layout.add_widget(button)  # Adicionando o botão ao layout de grade

        # Adicionando o layout de grade ao BottomSheet
        self.bottom_sheet_menu.add_widget(grid_layout) 
        self.bottom_sheet_menu.open()

def callback_for_menu_items(instance):
    print(f"Clicou no item: {instance.text}")

menu_items = [
    { "text": "Item 1",
      "on_release": callback_for_menu_items },
    { "text": "Item 2",
      "on_release": callback_for_menu_items },
    { "text": "Item 3",
      "on_release": callback_for_menu_items },
    { "text": "Item 4",
      "on_release": callback_for_menu_items },
]

if __name__ == "__main__":
    MainApp().run()