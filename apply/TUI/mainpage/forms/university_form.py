from textual.app import ComposeResult
from textual.widgets import Label, Input
from textual.containers import Container


class UniversityForm(Container):
    def compose(self) -> ComposeResult:
        yield Label("University Form")
        yield Input(placeholder="Country")
        yield Input(placeholder="University Name")