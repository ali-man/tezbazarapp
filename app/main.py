from kivy.app import App
from kivy.uix.image import AsyncImage


class MainApp(App):
    def build(self):
        return AsyncImage(source='http://hds5.tasx.uz/images/2020-04-09/1586387994_assasinfateofatl.jpg')


if __name__ == '__main__':
    MainApp().run()