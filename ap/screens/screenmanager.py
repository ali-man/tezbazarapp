from kivy.uix.screenmanager import ScreenManager

from ap.screens.shop.category import CategoryScreen
from ap.screens.shop.main import MainScreen
from ap.screens.profile import ProfileScreen
from ap.screens.shop.product import CardProduct

sm = ScreenManager()
screens = {
    'main': MainScreen,
    'profile': ProfileScreen,
    'category': CategoryScreen,
    'product': CardProduct,
}