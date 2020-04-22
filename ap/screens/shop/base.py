from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen


KV = """
<HeaderLayout>:
    size_hint: 1, .07
    pos_hint: {'x': 0, 'y': 0.93}
    canvas:
        Color:
            rgba: .47, .70, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Label:
        markup: True
        id: header_title
        pos_hint: {'x': 0, 'y': 0}
        padding: 10, 0
        size_hint: .4, 1
        halign: 'left'
        text_size: self.size[0], None
        text: 'TEZBAZAR'
        font_size: 16
        

<MenuLabel@Label>:
    markup: True
    font_size: '12sp'


<FooterLayout>:
    size_hint: 1, .07
    pos_hint: {'x': 0, 'y': 0}
    canvas:
        Color:
            rgba: .97, .97, .97, 1
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        MenuLabel:
            markup: True
            text: '[ref=][color=000000]Главная[/color][/ref]'
            on_ref_press: root.switch_screen('main')
        MenuLabel:
            markup: True
            text: '[ref=][color=000000]Каталог[/color][/ref]'
            on_ref_press: root.switch_screen('category')
        MenuLabel:
            text: '[color=000000]Поиск[/color]'
        MenuLabel:
            text: '[color=000000]999 тыс. сум[/color]'
        MenuLabel:
            text: '[color=000000]Профиль[/color]'
        

"""


Builder.load_string(KV)


class HeaderLayout(FloatLayout):
    pass


class FooterLayout(FloatLayout):
    def switch_screen(self, name_screen):
        App.get_running_app().switch_screen(name_screen)


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

