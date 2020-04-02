
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1


        self.Grid2 = GridLayout()
        self.Grid2.cols = 1
        self.Grid2.B = Button(text="click", font_size=20)
        self.Grid2.add_widget(self.Grid2.B)


        self.add_widget(Label(text="jgh"))

        self.G = Button(text="click", font_size=20)
        self.add_widget(Label(text="mlm"))

        self.add_widget(self.Grid2)




class MyApp(App):
    def build(self):
        return(MyGrid())
if __name__ == "__main__":
    MyApp().run()
