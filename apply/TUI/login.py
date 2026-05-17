import os

from textual import on
from textual.app import ComposeResult
from textual.containers import Center, VerticalGroup, HorizontalGroup
from textual.widgets import Label, Input, Button 
from textual.screen import Screen

from db.queries import verify_user

class LoginScreen(Screen):

    CSS_PATH = os.path.join("tcss", "loginpage.tcss")

    def __init__(self, db_session=None, name: str | None = None, id: str | None = None, classes: str | None = None) -> None:
        super().__init__(name, id, classes)
        self.__db_session = db_session

    def compose(self) -> ComposeResult:
        yield Center(
            VerticalGroup(
                Label('This is a label', id='label'),
                Input(placeholder='Username', id='username'),
                Input(placeholder='password', password=True, id='password'),
                Button('Login', classes='btn r1', id='login-btn'),
                HorizontalGroup(
                    Button('Register', classes='btn r2', id='register-btn'),
                    Button('Exit', classes='btn r2', id='exit-btn')
                ),
            classes='input'),
            id='wrapper'
        )

    @on(Button.Pressed, '#login-btn')
    def handle_login(self, event: Button.Pressed) -> None:
        username = self.query_one('#username', Input).value
        password = self.query_one('#password', Input).value

        if user := verify_user(self.__db_session, username, password):
            self.dismiss(user)
        else:
            self.query_one('#label', Label).update('Invalid username or password. Please try again.')

    @on(Button.Pressed, '#register-btn')
    def handle_register(self, event: Button.Pressed) -> None:
        self.dismiss('register')

    @on(Button.Pressed, '#exit-btn')
    def handle_exit(self, event: Button.Pressed) -> None:
        self.dismiss('exit')