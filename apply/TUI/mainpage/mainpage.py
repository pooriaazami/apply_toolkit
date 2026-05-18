import os

from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import (
    Header,
    Footer,
    Label,
    Input,
    TabbedContent,
    TabPane,
    ContentSwitcher,
    ListView,
    ListItem,
)

from .forms import *

class MainScreen(Screen):

    CSS_PATH = os.path.join("..", "tcss", "mainpage.tcss")

    def __init__(self, db_session, user):
        super().__init__()
        self.db_session = db_session
        self.user = user

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with TabbedContent():

            with TabPane("dashboard"):
                yield Label("Dashboard content goes here.")

            with TabPane("input"):
                with Container():
                    with Horizontal(id="input-container"):
                        yield ListView(
                            ListItem(Label("University"), id="university-item"),
                            ListItem(Label("Professor"), id="professor-item"),
                            id="input-list",
                        )

                        with ContentSwitcher(
                            initial="university-form",
                            id="input-switcher",
                        ):
                            yield UniversityForm(id="university-form")
                            yield ProfessorForm(id="professor-form")

                with Container(id='test-container'):
                    yield Label("input content goes here.")

            with TabPane("tasks"):
                yield Label('Tasks contest goes here.')

            with TabPane("assets"):
                yield Label("Assets content goes here.")

            with TabPane("settings"):
                yield Label("Settings content goes here.")

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        switcher = self.query_one("#input-switcher", ContentSwitcher)

        if event.item.id == "university-item":
            switcher.current = "university-form"

        elif event.item.id == "professor-item":
            switcher.current = "professor-form"