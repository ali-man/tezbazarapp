from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from ap.screens.shop.base import BaseScreen

KV = """
<CardProduct>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    HeaderLayout:
        id: header        
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                size: self.size
                pos: self.pos
        canvas.before:
            Color:
                rgba: .97, .97, .97, 1
            Rectangle:
                size: self.size
                pos: self.pos[0], self.pos[1] - 2
        BoxLayout
            Label:
                markup: True
                text: '[color=000000]<[/color]'
            Widget
            Label:
                markup: True
                text: '[color=000000]В закладки[/color]'
            Label:
                markup: True
                text: '[color=000000]:[/color]'
        
    BoxLayout:
        
    FooterLayout
"""

Builder.load_string(KV)


class CardProduct(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
