from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from ap.screens.shop.base import BaseScreen

KV = """
<ProductItem@BoxLayout>:
    orientation: 'vertical'
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    canvas.before:
        Color:
            rgba: .93, .93, .93, 1
        Rectangle:
            size: self.size
            pos: self.pos[0]+2, self.pos[1] - 2
    RelativeLayout:        
        AsyncImage:
            source: 'http://devuz.ru/media/product-item.jpg'
        Label:
            size_hint: 1, 1
            pos_hint: {'x': 0.25, 'y': 0.45}
            size: 200, 200
            pos: 200, 200
            pos: 1, 1
            markup: True
            text: '[color=000000]В закладки[/color]'
        Label:
            size_hint: 1, 1
            pos_hint: {'x': 0.25, 'y': -0.45}
            size: 200, 200
            pos: 200, 200
            pos: 1, 1
            markup: True
            text: '[color=000000]1 кг[/color]'
    Label:
        size_hint: 1, .1
        markup: True
        text: '[color=111111]12 000 сум[/color]'
        font_size: '16sp'
    Label:
        size_hint: 1, .15
        markup: True
        text: '[color=111111]Гречка упакованная отборная офигенная[/color]'
        max_lines: 2
        font_size: '12sp'
        text_size: 180, None    


<MainScreen>:
    HeaderLayout
    BoxLayout:
        size_hint: 1, .86
        pos_hint: {'x': 0, 'y': 0.07}        
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        AsyncImage:
            size_hint: 1, .64
            source: 'http://devuz.ru/media/1.jpg'
        BoxLayout:
            size_hint: 1, .12
            Label:
                markup: True
                text: '[ref=][color=111111]Популярные товары[/color][/ref]'
                font_size: '14sp'
                halign: 'left'
                text_size: self.size[0] - 20, None
                on_ref_press: root.on_clicked()
            Label:
                markup: True
                text: '[ref=`][color=77B200]Показать все[/color][/ref]'
                font_size: '14sp'
                halign: 'right'
                text_size: self.size[0] - 20, None
                on_ref_press: root.on_clicked()
        RecycleView:
            do_scroll_x: True
            do_scroll_y: False
            smooth_scroll_end: 20
            GridLayout:
                id: grid
                rows: 1
                col_force_default: True
                col_default_width: 240
                padding: 5, 0, 5, 0
                spacing: 5
                size_hint_x: None
                width: self.minimum_width
                ProductItem
                ProductItem
                ProductItem
                ProductItem
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem            
                ProductItem
        Widget:
            size_hint: 1, .5
    FooterLayout
"""

Builder.load_string(KV)


class MainScreen(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def switch_screen(self, name_screen):
        App.get_running_app().switch_screen(name_screen)

    def on_clicked(self):
        print('CLICKED!')
