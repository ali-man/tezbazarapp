from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


KV = """
<ProfileScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 100
        spacing: 20
        # canvas:
        #     Color:
        #         rgba: 1, 1, 1, 1
        #     Rectangle:
        #         size: self.size
        #         pos: self.pos
        TextInput:
            hint_text: 'Город'
        TextInput:
            hint_text: 'Тел. номер'
        Widget
        Button:
            text: 'Далее'
            on_press: root.switch_screen('main')
"""

# open('screens/kv/profile.kv', encoding='utf-8').read()
Builder.load_string(KV)


class ProfileScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    @staticmethod
    def switch_screen(name_screen):
        App.get_running_app().switch_screen(name_screen)
