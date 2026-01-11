from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label

from translate import Translator

class MyApp(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        Window.clearcolor = (26/255,26/255,26/255, 1)

        self.vls = ("Русский", "Английский", "Французский", "Испанский", "Немецкий", "Эстонский", "Финский", "Турецкий")
        self.lang = ""
        self.result = "Результат"

        self.spnr = Spinner(text="Язык", values=self.vls, size_hint=(0.3, None), height=44)
        self.text_input = TextInput(text="Введите текст", size_hint=(1, 0.6),
                                     font_size=16, background_color = (50/255,50/255,50/255, 1),
                                     foreground_color = (1, 1, 1, 1), font_name='Arial Rounded MT + Helvetica.ttf')
        
        self.text_output = TextInput(text=self.result, readonly=True, background_color = (50/255,50/255,50/255, 1), foreground_color = (1, 1, 1, 1), font_name='Arial Rounded MT + Helvetica.ttf')
        self.label_lang = Spinner(text="Определить",values=(""), size_hint=(0.3, None), height=44)

    def build(self):

        self.title = "переводчик"
        layout = BoxLayout(orientation="vertical")
        self.spnr.bind(text=self.on_spinner_select)
        self.btn = Button(text="Перевести", size_hint = (0.5, 0.2), pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        self.btn.bind(on_press=self.on_btn_press)
        
 
        layout.add_widget(self.label_lang)
        layout.add_widget(self.text_input)
        layout.add_widget(self.spnr)
        layout.add_widget(self.text_output)
        layout.add_widget(self.btn)

        return layout
    
    def on_spinner_select(self, spnr, text):

        self.lang = text

        if self.lang == "Русский":
            self.lang = "ru"
        if self.lang == "Английский":
            self.lang = "en"
        if self.lang == "Французский":
            self.lang = "fr"
        if self.lang == "Испанский":
            self.lang = "es"
        if self.lang == "Немецкий":
            self.lang = "de"
        if self.lang == "Эстонский":
            self.lang = "et"
        if self.lang == "Финский":
            self.lang = "fi"
        if self.lang == "Турецкий":
            self.lang = "tr"

        self.translator = Translator(to_lang=self.lang)
    
    def on_btn_press(self, btn, ):
        try:
            self.result = self.translator.translate(self.text_input.text)
        except:
            pass
        self.text_output.text = self.result


if __name__ == '__main__':
    MyApp().run()