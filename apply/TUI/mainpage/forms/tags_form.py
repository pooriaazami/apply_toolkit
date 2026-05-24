from textual.app import ComposeResult
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Input, Button, Label, ListView, ListItem
from textual.containers import Container, HorizontalGroup

from db.queries import add_tag, get_tags_by_user


class TagsForm(Container):

    class TagAdded(Message):
        pass

    def __init__(self, db_session, active_user,*children: Widget, name: str | None = None, id: str | None = None, classes: str | None = None, disabled: bool = False, markup: bool = True) -> None:
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        self.__db_session = db_session
        self.__active_user = active_user

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Input(placeholder='Tag name', id='tags-form__tag-name'),
            Button('Add', id='tags-form__add-btn'),
            
        )

        yield Label('', id='tags-form__message')

        yield ListView(
            *[ListItem(Label(tag.name)) for tag in get_tags_by_user(self.__db_session, self.__active_user.id)],
            id='tags-form__tag-list'
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'tags-form__add-btn':
            tag_name = self.query_one('#tags-form__tag-name', Input).value

            if not tag_name:
                self.query_one('#tags-form__message', Label).update("Please enter a tag name.")
                return
            
            new_tag = add_tag(self.__db_session, tag_name, self.__active_user.id)

            self.query_one('#tags-form__tag-name', Input).value = ""
            if new_tag:
                self.query_one('#tags-form__tag-list', ListView).append(ListItem(Label(new_tag.name)))
                self.query_one('#tags-form__message', Label).update(f"Added tag: {new_tag.name}")
                self.post_message(self.TagAdded())
            else:
                self.query_one('#tags-form__message', Label).update("Failed to add tag.")