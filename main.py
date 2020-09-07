# Android - Material Design - Gardening Toolset App


########################################################################################################################

# Python Imports
import sys
import webbrowser

########################################################################################################################

# Kivy Imports
import kivy
from kivy import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FallOutTransition

########################################################################################################################

# KivyMD Imports

import kivymd
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.list import OneLineAvatarIconListItem, OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase

########################################################################################################################
# Other Imports
########################################################################################################################


# Config Set.

kivy.require("1.11.1") # If issues - use 1.10.1 - apply same in .spec
Window.size = (540, 960)
Config.set('graphics', 'resizable', True)

# kivy.metrics.MetricsBase.dpi = '440'




########################################################################################################################
"""Plants_Screen Class Creation"""
########################################################################################################################
#TODO create iteration function over vegetable names to create all classes - to replace individual class replacement

class Label_1(MDLabel):
    pass

class Label_2(MDLabel):
    pass

class Icon_1(MDIcon):
    pass

class Variety_Info_Item(OneLineIconListItem):
    pass

class PlantLabels(MDLabel):
    pass

class ListLetters(MDLabel):
    pass

class PlantsListContainer(MDCard):
    pass

class PlantsListContent(MDBoxLayout):
    pass

class Plants_Home(MDScreen) :
    pass

class Apples(MDScreen):
    pass

class Asparagus(MDScreen):
    pass

class Aubergine(MDScreen):
    pass

class Basil(MDScreen):
    pass

class Broccoli(MDScreen):
    pass

class Carrots(MDScreen) :
    class Carrot_Wiki(FloatLayout, MDTabsBase):
        def adelaide_open(self):
            webbrowser.open_new('https://www.thompson-morgan.com/p/carrot-adelaide-f1-hybrid/781TM')
        def nantes_open(self):
            webbrowser.open_new('https://www.suttons.co.uk/Gardening/Vegetable-Seeds/Popular-Vegetable-Seeds/'
                                'Carrot-Seeds/Carrot-Seeds---Early-Nantes-5_MH266.htm')
        def chantenay_open(self):
            webbrowser.open_new('https://www.suttons.co.uk/Gardening/Vegetable-Seeds/Popular-Vegetable-Seeds/'
                                'Carrot-Seeds/Carrot-Seeds---Chantenay-Red-Cored-2_157335.htm')
    class Carrot_Guide(FloatLayout, MDTabsBase):
        pass
    class Carrot_Plants(FloatLayout, MDTabsBase):
        data = {
            'carrot': 'Add Plant'
        }
    class Carrot_Photos(FloatLayout, MDTabsBase):
        pass

class Tabs(MDTabsBase):
    pass

class Screen2_2(MDScreen) :
    pass


class Screen2_3(MDScreen) :
    pass

class Screen2_4(MDScreen) :
    pass


########################################################################################################################
"""Screen Class Creation"""
########################################################################################################################

class HomeScreen(MDScreen) :
    pass


class PlantsScreen(MDScreen) :
    def on_enter(self) :
        self.manager.current = 'Plants_Home'


########################################################################################################################
"""App Widgets Class Creation"""
########################################################################################################################

class ItemConfirm(OneLineAvatarIconListItem) :
    divider = None

    def set_icon(self, instance_check) :
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list :
            if check != instance_check :
                check.active = False

########################################################################################################################
""".kv File Loading"""
########################################################################################################################
#TODO iteration function to Builder.loadfile all .kv within kv folder

Builder.load_file('kv files/Plants_Screen.kv')
Builder.load_file('kv files/sm2_Screens.kv')
Builder.load_file('kv files/Apples.kv')
Builder.load_file('kv files/Asparagus.kv')
Builder.load_file('kv files/Aubergine.kv')
Builder.load_file('kv files/Basil.kv')
Builder.load_file('kv files/Broccoli.kv')
Builder.load_file('kv files/Carrots.kv')
# Builder.load_file('kv files/Tasks_Screen.kv')
# Builder.load_file('kv files/Wiki_Screen.kv')
# Builder.load_file('kv files/Settings_Screen.kv')

########################################################################################################################

# MainLoop

class GardenTools(MDApp) :
    dialog = None

    def build(self) :

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.accent_pallette = "Yellow"
        self.theme_cls.accent_hue = "600"



        return Builder.load_file('kv files/main.kv')





GardenTools().run()
