from textual.app import ComposeResult
from textual.widgets import Label, Input, Select, SelectionList
from textual.containers import Container


class TagsForm(Container):
    def compose(self) -> ComposeResult:
        yield Label('Tags Form')