from textual.containers import VerticalGroup
from textual.widgets import Label, Header, Footer, Tabs, Tab
from textual.screen import Screen

class MainScreen(Screen):
    def __init__(self, db_session, user, name: str | None = None, id: str | None = None, classes: str | None = None) -> None:
        super().__init__(name, id, classes)
        self.__db_session = db_session
        self.__user = user

    def compose(self):
        yield Header()
        yield Footer()

        yield Tabs(
                Tab('dashboard', id='dashboard-tab'),
                Tab('desk', id='desk-tab'),
                Tab('assets', id='assets-tab'),
                Tab('settings', id='settings-tab'),
            )   
    