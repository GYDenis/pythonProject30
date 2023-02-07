import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Application(App):
    def build(self):

        but_together = BoxLayout()

        my_but = Button(text="DENIS.travis.yml", font_size=30, background_color="cyan")

        but_together.add_widget(my_but)


        return but_together

if __name__== "__main__":

    Application().run()


