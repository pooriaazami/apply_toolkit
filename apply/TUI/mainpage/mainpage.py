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
        self.__db_session = db_session
        self.__user = user

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
                            ListItem(Label("Country"), id="country-item"),
                            ListItem(Label('Tags'), id='tags-item'),
                            ListItem(Label("University"), id="university-item"),
                            ListItem(Label("Professor"), id="professor-item"),
                            id="input-list",
                        )

                        with ContentSwitcher(
                            initial="country-form",
                            id="input-switcher",
                        ):
                            yield CountryForm(id='country-form', db_session=self.__db_session, active_user=self.__user)
                            yield TagsForm(id='tags-form', db_session=self.__db_session, active_user=self.__user)
                            yield UniversityForm(id="university-form", db_session=self.__db_session, active_user=self.__user)
                            yield ProfessorForm(id="professor-form", db_session=self.__db_session, active_user=self.__user)

                # with Container(id='test-container'):
                #     yield Label("input content goes here.")

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

        elif event.item.id == 'country-item':
            switcher.current = 'country-form'

        elif event.item.id == 'tags-item':
            switcher.current = 'tags-form'

    def on_country_form_country_added(self, message: CountryForm.CountryAdded):
        university_form = self.query_one("#university-form", UniversityForm)
        university_form.refresh_countries()

    def on_tags_form_tag_added(self, message: TagsForm.TagAdded):
        professor_form = self.query_one("#professor-form", ProfessorForm)
        professor_form.refresh_tags()

    def on_university_form_university_added(self, message: UniversityForm.UniversityAdded):
        professor_form = self.query_one("#professor-form", ProfessorForm)
        professor_form.refresh_universities()