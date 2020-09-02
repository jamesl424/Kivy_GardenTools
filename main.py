# Android - Material Design - Gardening Toolset App


########################################################################################################################

# Python Imports

########################################################################################################################

# Kivy Imports


from kivy.core.window import Window
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FallOutTransition

########################################################################################################################

# KivyMD Imports


from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase

########################################################################################################################
# Other Imports
########################################################################################################################


# Config Set.


Window.size = (540, 960)

# kivy.metrics.MetricsBase.dpi = '440'




########################################################################################################################
"""Plants_Screen Class Creation"""
########################################################################################################################
class Label_1(MDLabel):
    pass

class Icon_1(MDIcon):
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

class Carrots(MDScreen) :
    class Carrot_Wiki(FloatLayout, MDTabsBase):
        pass
    class Carrot_Plants(FloatLayout, MDTabsBase):
        pass
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

Builder.load_file('.kv files/Plants_Screen.kv')
Builder.load_file('.kv files/sm2_Screens.kv')
Builder.load_file('.kv files/Apples.kv')
Builder.load_file('.kv files/Carrots.kv')
# Builder.load_file('.kv files/Tasks_Screen.kv')
# Builder.load_file('.kv files/Wiki_Screen.kv')
# Builder.load_file('.kv files/Settings_Screen.kv')

########################################################################################################################

# MainLoop

class GardenTools(MDApp) :
    dialog = None

    def build(self) :
        return Builder.load_file('.kv files/main.kv')





GardenTools().run()
