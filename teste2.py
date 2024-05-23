from kivymd.app import MDApp
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.list import OneLineListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.lang import Builder

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("teste2.kv")

    def show_backdrop1(self, instance):
        self.backdrop.set_state("open")
        self.backdrop.left_action = lambda: self.backdrop.set_state("close")
        self.backdrop.right_action = lambda: self.backdrop.set_state("open")

        self.items1 = ["Item 1", "Item 2", "Item 3"]
        self.selected_items1 = []

        # Adicionar os itens ao left_action_items do backdrop
        for item in self.items1:
            item_box = MDBoxLayout(orientation='horizontal', spacing=10)
            checkbox = MDCheckbox(size_hint_x=None, width=30)
            checkbox.bind(active=self.on_checkbox_active1)
            item_label = OneLineListItem(text=item)
            item_box.add_widget(checkbox)
            item_box.add_widget(item_label)
            self.backdrop.left_action_items.add_widget(item_box)

    def on_checkbox_active1(self, instance, value):
        if value:
            self.selected_items1.append(instance.parent.children[1].text)
        else:
            self.selected_items1.remove(instance.parent.children[1].text)
        self.selected_items_label1.text = f"Selected: {', '.join(self.selected_items1)}"

    def show_backdrop2(self, instance):
        self.backdrop.set_state("open")
        self.backdrop.left_action = lambda: self.backdrop.set_state("close")
        self.backdrop.right_action = lambda: self.backdrop.set_state("open")

        self.items2 = ["Item 4", "Item 5", "Item 6", "Item 7", "Item 8"]
        self.selected_items2 = []

        # Adicionar os itens ao left_action_items do backdrop
        for item in self.items2:
            item_box = MDBoxLayout(orientation='horizontal', spacing=10)
            checkbox = MDCheckbox(size_hint_x=None, width=30)
            checkbox.bind(active=self.on_checkbox_active2)
            item_label = OneLineListItem(text=item)
            item_box.add_widget(checkbox)
            item_box.add_widget(item_label)
            self.backdrop.left_action_items.add_widget(item_box)

    def on_checkbox_active2(self, instance, value):
        if value:
            self.selected_items2.append(instance.parent.children[1].text)
        else:
            self.selected_items2.remove(instance.parent.children[1].text)
        self.selected_items_label2.text = f"Selected: {', '.join(self.selected_items2)}"