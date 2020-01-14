from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class PosButtons(Widget):
    def __init__(self, **kwargs):
        super(PosButtons, self).__init__(**kwargs)


class PosGroups(Widget):
    def __init__(self, **kwargs):
        super(PosGroups, self).__init__(**kwargs)


class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)


class PosApp(App):
    def build(self):
        return ContainerBox()


if __name__ == '__main__':
    PosApp().run()