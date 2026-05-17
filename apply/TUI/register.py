import os

from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Center, VerticalGroup, HorizontalGroup
from textual.widgets import Label, Input, Button

from db.queries import create_user

class RegisterScreen(Screen):
    CSS_PATH = CSS_PATH = os.path.join("tcss", "registerpage.tcss")

    def __init__(self, db_session=None, name: str | None = None, id: str | None = None, classes: str | None = None) -> None:
        super().__init__(name, id, classes)
        self.__db_session = db_session

    def compose(self) -> ComposeResult:
        yield Center(
            VerticalGroup(
                Label('There is not any registered user. Please register first.', id='label'),
                Input(placeholder='Username', id='username'),
                Input(placeholder='password', password=True, id='password'),
                Input(placeholder='Confirm password', password=True, id='confirm-password'),
                HorizontalGroup(
                    Button('Register and Enter', classes='btn', id='register-btn'),
                    Button('Exit', classes='btn', id='exit-btn')
                ),
            classes='input'),
            id='wrapper'
        )

    @on(Button.Pressed, '#register-btn')
    def button_pressed(self, event: Button.Pressed) -> None:
        username = self.query_one('#username', Input).value
        password = self.query_one('#password', Input).value
        confirm_password = self.query_one('#confirm-password', Input).value

        if password != confirm_password:
            self.query_one('#label', Label).update('Passwords do not match. Please try again.')
            return
        else:
            user = create_user(self.__db_session, username, password)
            self.dismiss(user)

    @on(Button.Pressed, '#exit-btn')
    def exit_pressed(self, event: Button.Pressed) -> None:
        self.dismiss('exit')