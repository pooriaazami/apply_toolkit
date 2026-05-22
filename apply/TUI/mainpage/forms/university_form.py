from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label, Input, Select, SelectionList
from textual.containers import Container, HorizontalGroup

from db.queries import get_countries_by_user


class UniversityForm(Container):

    def __init__(self, db_session, active_user, *children: Widget, name: str | None = None, id: str | None = None, classes: str | None = None, disabled: bool = False, markup: bool = True) -> None:
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)

        self.__db_session = db_session
        self.__active_user = active_user

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Select(
                options=[
                    (country.name, country.code) for country in get_countries_by_user(self.__db_session, self.__active_user.id)
                ],
                id='university-form__country-select'
            ),
            Input(placeholder="University Name", id='university-form__university-name')
        )

    def on_mount(self):
        self.refresh_countries()
    
    def refresh_countries(self):
        select = self.query_one("#university-form__country-select", Select)

        select.clear()

        countries = get_countries_by_user(
            self.__db_session,
            self.__active_user.id
        )

        select.set_options([(country.name, country.code) for country in countries])
