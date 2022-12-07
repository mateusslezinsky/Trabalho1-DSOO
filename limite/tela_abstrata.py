from abc import ABC, abstractmethod
import PySimpleGUI as sg


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    def text(self, text, visible=True, fontSize=18):
        return sg.Text(text, visible=visible, font=("Helvetica", fontSize))

    def input_radio(self, text, key, default=False, fontSize=18):
        return sg.Radio(text, "RD1", default=default, key=key, font=("Helvetica", fontSize))

    def confirm_button(self, text="Confirmar", color="green"):
        return sg.Button(text, button_color=color, font=("Helvetica", 18))

    def cancel_button(self, cancel_text="Sair"):
        return sg.Cancel(cancel_text, button_color="red", font=("Helvetica", 18))

    def input_text(self, data, key):
        return sg.InputText(data, key=key, font=("Helvetica", 18))

    def slider(self, range=(1, 100), value=1, key=""):
        return sg.Slider(range=range, orientation="h", default_value=value, key=key)

    def init_components(self, text_dict):
        sg.ChangeLookAndFeel("DarkTeal4")

        layout = [
            [self.text(text_dict["title"], fontSize=25)],
            [self.input_radio(text_dict["key1"], key="1")],
            [self.input_radio(text_dict["key2"], key="2")],
            [self.input_radio(text_dict["key3"], key="3")
             if text_dict["key3"] else []],
            [self.input_radio(text_dict["key4"], key="4")
             if text_dict["key4"] else []],
            [self.input_radio(text_dict["key5"], key="5")
             if text_dict["key5"] else []],
            [self.input_radio(text_dict["key0"], key="0")],
            [self.confirm_button(),
             self.cancel_button(text_dict["key0"])],
        ]
        self.__window = sg.Window(text_dict["title"]).Layout(layout)
