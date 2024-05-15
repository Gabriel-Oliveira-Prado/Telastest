from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDCard:
        radius: 36
        md_bg_color: "grey"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .4, .8

        FitImage:
            source: "bg.jpg"
            size_hint_y: .35
            pos_hint: {"top": 1}
            radius: 36, 36, 0, 0
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()