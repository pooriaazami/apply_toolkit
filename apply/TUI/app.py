from textual.app import App
from textual.widgets import Header, Footer

from db.queries import get_number_of_users

from . import LoginScreen


class ApplyApp(App):

    TITLE = "Apply Toolkit"

    def __init__(self, db_session=None):
        super().__init__()
        self.__db_session = db_session

    def on_mount(self):
        if get_number_of_users(self.__db_session) == 0:
            self.push_screen(LoginScreen(db_session=self.__db_session))
            print('User created!')
        else:
            print('Done!')
            self.exit()
            # self.push_screen(MainScreen())

    def compose(self):
        yield Header()
        yield Footer()