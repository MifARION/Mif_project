from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')


class Calculator(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == '0'):
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += '*'
        elif str(instance.text).lower() == '√':
            self.formula += '**'
        elif str(instance.text).lower() == '÷':
            self.formula += '/'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = '0'

    def menu(self, instance):
        self.formula = '0'
        self.update_label()

    def clear_one(self, instance):
        self.formula = self.formula[:-1] or '0'
        self.update_label()

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical')
        gl = GridLayout(cols=4, rows=6, padding=[5], spacing=3, row_force_default=True, row_default_height=52.65)

        self.lbl = Label(text='0',
                         font_size=40,
                         halign='right',
                         size_hint=(1, .4),
                         text_size=(300 - 10, 400 * .4 - 10),
                         valign='center')
        gl.add_widget(
            Button(text='\u00a8', on_press=self.menu, background_color=[.65, .65, .65, 1], background_normal='',
                   font_size=35))
        gl.add_widget(
            Button(text='√', on_press=self.add_operation, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=21))
        gl.add_widget(
            Button(text='÷', on_press=self.add_operation, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=21))
        gl.add_widget(
            Button(text='\u00ab', on_press=self.clear_one, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=25))

        gl.add_widget(Button(text='7', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='8', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='9', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(
            Button(text='x', on_press=self.add_operation, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=21))

        gl.add_widget(Button(text='4', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='5', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='6', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(
            Button(text='-', on_press=self.add_operation, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=30))

        gl.add_widget(Button(text='1', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='2', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='3', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(
            Button(text='+', on_press=self.add_operation, background_color=[1, .58, 0, 1], background_normal='',
                   font_size=21))

        gl.add_widget(
            Button(text='00', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                   font_size=21))
        gl.add_widget(Button(text='0', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(Button(text='.', on_press=self.add_number, background_color=[.2, .2, .2, 1], background_normal='',
                             font_size=21))
        gl.add_widget(
            Button(text='=', on_press=self.result, background_color=[1, .58, 0, 1], background_normal='', font_size=21))

        bl.add_widget(self.lbl)
        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    Calculator().run()

