from kivy.app import App
from kivy.lang import Builder
from ap.screens.shop.base import BaseScreen

KV = """
<ProductItemFromCategories@BoxLayout>:
    padding: 5
    spacing: 10
    AsyncImage:
        size_hint: .4, 1
        source: 'http://devuz.ru/media/product-item.jpg'
    BoxLayout:
        size_hint: .6, 1
        orientation: 'vertical'        
        Label:
            markup: True
            text: '[color=111111]Ядрица гречневая "Мистраль"[/color]'
            font_size: '14sp'
            halign: 'left'
            text_size: self.size[0], None
        Label:
            markup: True
            text: '[color=111111]12 000 сум[/color]'
            font_size: '14sp'
            halign: 'left'
            text_size: self.size[0], None
        Widget
        BoxLayout:            
            Button:
                markup: True
                text: '[color=77B200]-[/color]'
                background_color: 1, 1, 1, 1
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: .93, .93, .93, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos[0]+2, self.pos[1] - 2
            Widget
            Label:
                markup: True
                text: '[color=111111]9 999[/color]'
            Widget
            Button:
                markup: True
                text: '[color=77B200]+[/color]'
                background_color: 1, 1, 1, 1
                background_normal: ''
                canvas.before:
                    Color:
                        rgba: .93, .93, .93, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos[0]+2, self.pos[1] - 2
            Widget
            Widget
            Widget
            
    BoxLayout:
        size_hint: .08, 1
        orientation: 'vertical'        
        Label:
            markup: True
            text: '[color=111111]00[/color]'
            halign: 'right'
            text_size: self.size[0], None
        Widget


<CategoryScreen>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    HeaderLayout:
        id: header
    RecycleView:
        size_hint: 1, .86
        pos_hint: {'x': 0, 'y': 0.07}
        do_scroll_x: False
        do_scroll_y: True
        smooth_scroll_end: 20        
        GridLayout:
            id: grid
            cols: 1
            row_force_default: True
            row_default_height: 100
            padding: 5
            spacing: 5
            size_hint_y: None
            height: self.minimum_height
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
            ProductItemFromCategories
    FooterLayout
"""

Builder.load_string(KV)


class CategoryScreen(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.header.ids.header_title.text = 'Крупы'

    @staticmethod
    def switch_screen(name_screen):
        App.get_running_app().switch_screen(name_screen)
