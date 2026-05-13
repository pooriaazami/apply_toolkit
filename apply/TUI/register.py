from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Center, VerticalGroup, HorizontalGroup
from textual.widgets import Label, Input, Button

class LoginScreen(Screen):
    CSS_PATH = "tcss/loginpage.tcss"

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

    @on(Button.Pressed, '.btn')
    def button_pressed(self, event: Button.Pressed) -> None:
        username = self.query_one('#username', Input).value
        password = self.query_one('#password', Input).value
        confirm_password = self.query_one('#confirm-password', Input).value

        if password != confirm_password:
            self.query_one('#label', Label).update('Passwords do not match. Please try again.')
            return
        else:
            #TODO: Create user and save to database
            pass

    @on(Button.Pressed, '#exit-btn')
    def exit_pressed(self, event: Button.Pressed) -> None:
        self.app.exit()