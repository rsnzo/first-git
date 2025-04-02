from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class LikeApp(App):
    def build(self):
        self.mainBox = BoxLayout(orientation="vertical")
        self.lbl_title  = Label(text='rate this picture', font_size= 30)
        self.image = Image(source="f11cfe34ed1a91e120326b2ea06296b2.jpg")
        btn_layout = BoxLayout(size_hint =[1,0.7])

        self.stars = []

        for i in range(5):
            btn = Button(text = f"{i+1}", 
                         color=[0,0,0,0], 
                         background_normal = "beginner_git\star0.png",
                         background_down = "beginner_git\star0.png",
                         on_press = self.rate)
            self.stars.append(btn)
            btn_layout.add_widget(btn)

        self.mainBox.add_widget(self.lbl_title)
        self.mainBox.add_widget(self.image)


        self.mainBox.add_widget(btn_layout)


        return self.mainBox
    
    def rate(self,btn):
        index = int(btn.text) - 1
        for i in range(len(self.stars)):
            if i <=index:
                self.stars[i].background_normal = "beginner_git/star1.png"
                self.stars[i].background_down = "beginner_git/star1.png" 
            else:
                self.stars[i].background_normal = "beginner_git/star0.png"
                self.stars[i].background_down = "beginner_git/star0.png" 

LikeApp().run()