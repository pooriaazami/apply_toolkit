from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Input, Button, Label, ListView, ListItem
from textual.containers import Container, HorizontalGroup

from db.queries import add_country, fetch_all_countries

class CountryForm(Container):

    def __init__(self, db_session, user, *children: Widget, name: str | None = None, id: str | None = None, classes: str | None = None, disabled: bool = False, markup: bool = True) -> None:
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        self.__db_session = db_session
        self.__user = user

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Input(placeholder='Country name', id='country-form__country-name'),
            Input(placeholder='Country code', id='country-form__country-code')
        )

        yield HorizontalGroup(
            Button('Add', id='country-form__add-btn'),
            Label('', id='country-form__message')
        )

        yield ListView(
            *[ListItem(Label(country)) for country in fetch_all_countries(self.__db_session)],
            id='country-form__country-list'
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'country-form__add-btn':
            country_name = self.query_one('#country-form__country-name', Input).value
            country_code = self.query_one('#country-form__country-code', Input).value

            if not country_name or not country_code:
                self.query_one('#country-form__message', Label).update("Please fill in all fields.")
                return
            
            new_country = add_country(self.__db_session, country_name, country_code, self.__user.id)
            if new_country:
                self.query_one('#country-form__message', Label).update(f"Added country: {new_country.name} ({new_country.code})")
                self.query_one('#country-form__country-name', Input).value = ""
                self.query_one('#country-form__country-code', Input).value = ""

                self.query_one('#country-form__country-list', ListView).append(ListItem(Label(f'{new_country.name} | ({new_country.code})')))
