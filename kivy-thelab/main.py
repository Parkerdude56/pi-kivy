from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout





class WidgetsExample(GridLayout):
    count = 0
    button_off = True
    my_text = StringProperty("0 !")
    text_input_str = StringProperty("foo")
    # slider_value_txt = StringProperty("Value")

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        self.button_off = not self.button_off
        print(self.button_off)
        if self.button_off:
            print("bool=true")
        else:
            print(self.button_off)
        # if widget.state == "normal":
        #     widget.text = "OFF"
        #     button_off = True
        #     print(button_off)
        #     print(self.count)
        # else:
        #     widget.text = "ON"
        #     button_off = False
        #     print(button_off)
        #     print(self.count)

    def on_button_click(self):
        print("Button Clicked")
        #if not self.button_off:
        print(self.button_off)
        if self.button_off:
            print("boolean is true")
        else:
            print("boolean is false")
            self.count += 1
        self.my_text = str(self.count) + " !"

    def on_button_release(self):
        print("Button Released")

    def on_switch_active(self, widget):
        print("Switch: " + str(int(widget.active)))

    # def on_slider_value(self, widget):
        # print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-tb"
        for i in range(0, 100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass



TheLabApp().run()

