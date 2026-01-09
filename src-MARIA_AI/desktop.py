from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.label import Label # Example UI element



#Window.clearcolor(0,0,0,0)

class MariaAiApp(App):
    def build(self):
        root_layout = FloatLayout()
        video = Video(source="futuristic-interface.mp4", state="play" , size=(1,1))
        video.options = {'eos': 'loop'}
        video.allow_stretch = True
        root_layout.add_widget(video)

        main_ui_layout = FloatLayout()  # Or any other layout for your main UI
        main_ui_layout.add_widget(Label(text="MARIA AI",
                                        size_hint=(1,1),
                                        size=(500, 500),
                                        font_size="20sp",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        color=(1, 1, 1, 1)))
        root_layout.add_widget(main_ui_layout)
        return root_layout
        label = Label(text='Hello World',font_size='80sp', color=(0,1,0,1))
        return label

if __name__ == '__main__':
    MariaAiApp().run()
