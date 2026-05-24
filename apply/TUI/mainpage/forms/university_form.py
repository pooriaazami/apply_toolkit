from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Label, Input, Select, SelectionList, ListView, ListItem
from textual.containers import Container, HorizontalGroup

from db.queries import get_countries_by_user, add_university, get_universities_by_user


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
                id='university-form__country-select',
                prompt='Select the country where the university is located'
            ),
            Input(placeholder="University Name", id='university-form__university-name')
        
        )
        
        yield HorizontalGroup(
            Button("Add", id='university-form__add-btn'),
            Label("", id='university-form__message')
        )

        yield ListView(
            *[
                ListItem(Label(f"{university.name} | ({university.country.name})"))
                for university in get_universities_by_user(self.__db_session, self.__active_user.id)
            ],
            id='university-form__university-list'
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'university-form__add-btn':
            university_name = self.query_one('#university-form__university-name', Input).value
            country_id = self.query_one('#university-form__country-select', Select).value

            if not country_id or not university_name:
                self.query_one('#university-form__message', Label).update("Please fill in all fields.")
                return
            
            new_university = add_university(self.__db_session, university_name, country_id)
            if new_university:
                self.query_one('#university-form__message', Label).update("University added successfully.")
                self.query_one('#university-form__university-name', Input).value = ""
                self.query_one('#university-form__university-list', ListView).append(ListItem(Label(f"{new_university.name} | ({new_university.country.name})")))
            else:
                self.query_one('#university-form__message', Label).update("Failed to add university.")

    def on_mount(self):
        self.refresh_countries()
    
    def refresh_countries(self):
        select = self.query_one("#university-form__country-select", Select)

        select.clear()

        countries = get_countries_by_user(
            self.__db_session,
            self.__active_user.id
        )

        select.set_options([(country.name, country.id) for country in countries])
