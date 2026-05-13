from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Center, VerticalGroup
from textual.widgets import Header, Footer, Label, Input


from TUI import LoginScreen

Users = []

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Center(
            Label('Welcome to the Apply Toolkit!')
        )

class ApplyApp(App):

    TITLE = "Apply Toolkit"

    def on_mount(self):
        if len(Users) == 0:
            self.push_screen(LoginScreen())
        else:
            self.push_screen(MainScreen())

    def compose(self):
        yield Header()
        yield Footer()

def main():
    app = ApplyApp()
    app.run()   

if __name__ == "__main__":
    main()