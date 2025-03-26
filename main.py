from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class LikeApp(App):
    def build(self):
        self.mainBox = BoxLayout(orientation="vertical")
        self.lbl_title  = Label(text='rate this picture')
        self.image = Image(source="f11cfe34ed1a91e120326b2ea06296b2.jpg")
        btn_layout = BoxLayout(size_hint =[1,0.2])

        btn_like = Button(text="Like",font_size=24,size_hint=[0.45,0.7],)
        btn_dislike = Button(text="Like",font_size=24,size_hint=[0.45,0.7],)

        self.mainBox.add_widget(self.lbl_title)
        self.mainBox.add_widget(self.image)

        btn_layout.add_widget(btn_like)
        btn_layout.add_widget(btn_dislike)

        self.mainBox.add_widget(btn_layout)
LikeApp().run()