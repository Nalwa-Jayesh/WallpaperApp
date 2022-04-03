import kivy
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (310, 580)


class Wallpaper(MDApp):
    def build(self):
        return Builder.load_file("wallpaper.kv")

    def search(self, search_text):
        if search_text != "":
            self.root.ids.search_label.text = search_text
            self.root.ids.screen_manager.current = "search_results"
            for i in range(100):
                result = LoaderImage(source=f"https://source.unsplash.com/140x200/?{search_text}={i}",
                                    size_hint=(None, None), size=("140dp", "200dp"))
                self.root.ids.search_list.add_widget(result)

    def clear_results(self):
        self.root.ids.search_text.text = ""
        self.root.ids.search_list.clear_widgets(None)

    def change_color(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(3):
                if "nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = kivy.utils.rgba(253, 175, 177, 255)
                else:
                    self.root.ids[f"nav_icon{i+1}"].text_color = kivy.utils.rgba(222, 222, 222, 255)


class LoaderImage(AsyncImage):
    pass

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Poppins-SemiBold.ttf")
    Wallpaper().run()
