from kivy.app import App
from kivy.uix.screenmanager import ScreenManagerException
from kivy.config import Config

from ap.screens.screenmanager import sm, screens


Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 800)
Config.write()


class MainApp(App):
    title = 'TEZBAZAR'
    screen_manager = None

    def init_app(self):
        self.screen_manager = sm
        self.switch_screen('product')

    def switch_screen(self, screen_name):
        if screen_name in screens.keys():
            screen = screens[screen_name](name=screen_name)
            self.screen_manager.switch_to(screen)
            return
        else:
            raise ScreenManagerException(f'Screen {screen_name} not found')

    def build(self):
        self.init_app()
        return self.screen_manager


if __name__ in ('__main__', '__android__'):
    MainApp().run()
