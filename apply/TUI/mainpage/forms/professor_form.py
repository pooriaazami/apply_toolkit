from textual.app import ComposeResult
from textual.widgets import Label, Input, TextArea
from textual.containers import Container

class ProfessorForm(Container):
    def compose(self) -> ComposeResult:
        # yield Label("Professor Form")
        yield Input(placeholder="Professor Name")
        yield Input(placeholder="Email")
        yield Input(placeholder="University")
        yield TextArea(placeholder="Notes")