from textual.app import App
from textual.widgets import Header, Footer

from . import LoginScreen


class ApplyApp(App):

    TITLE = "Apply Toolkit"

    def on_mount(self):
        # if len(Users) == 0:
        self.push_screen(LoginScreen())
        # else:
        #     self.push_screen(MainScreen())

    def compose(self):
        yield Header()
        yield Footer()