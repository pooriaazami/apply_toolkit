from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Label, Input, SelectionList, TextArea, ListView, ListItem, Select
from textual.containers import Container, HorizontalGroup, VerticalGroup

from db.queries import get_universities_by_user, get_tags_by_user, add_professor, add_professor_tags, get_professors_by_user

class ProfessorForm(Container):

    def __init__(self, db_session, active_user, *children: Widget, name: str | None = None, id: str | None = None, classes: str | None = None, disabled: bool = False, markup: bool = True) -> None:
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)

        self.__db_session = db_session
        self.__active_user = active_user

    def compose(self) -> ComposeResult:
        yield Label("", id='professor-form__message-label')
        yield VerticalGroup(
            HorizontalGroup(
                Input(placeholder="Professor Name", id='professor-form__name'),
                Input(placeholder="Email", id='professor-form__email'),
                id='professor-form__input-group-name-email'
            ),
            HorizontalGroup(
                VerticalGroup(
                    Select(
                        options=[(uni.name, uni.id) for uni in get_universities_by_user(self.__db_session, self.__active_user.id)],
                        id='professor-form__university',
                        prompt='Select the university the professor is affiliated with'
                    ),
                    TextArea(placeholder="Notes", id='professor-form__notes'),
                    Button("Add Professor", id='professor-form__add-btn'),
                ),
                VerticalGroup(
                    SelectionList(
                        *[(tag.name, tag.id) for tag in get_tags_by_user(self.__db_session, self.__active_user.id)],
                        id='professor-form__tags-selection'
                    ),
                    id="professor-form__tags-column"
                )
            ),
            id='professor-form__input-group-all'
        )

        yield ListView(
                *[
                    ListItem(Label(f"{prof.name} @ {prof.university.name}"))
                    for prof in get_professors_by_user(self.__db_session, self.__active_user.id)
                ],
            id='professor-form__professor-list'
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'professor-form__add-btn':
            name_input = self.query_one('#professor-form__name', Input)
            email_input = self.query_one('#professor-form__email', Input)
            university_select = self.query_one('#professor-form__university', Select)
            notes_input = self.query_one('#professor-form__notes', TextArea)
            tags_selection = self.query_one('#professor-form__tags-selection', SelectionList)

            name = name_input.value
            email = email_input.value
            university_id = university_select.value
            notes = notes_input.text
            selected_tag_ids = tags_selection.selected

            if len(selected_tag_ids) == 0:
                message_label = self.query_one('#professor-form__message-label', Label)
                message_label.update("Please select at least one tag for the professor.")
                return
            
            if not name or not email or not university_id:
                message_label = self.query_one('#professor-form__message-label', Label)
                message_label.update("Please fill in all required fields (name, email, university).")
                return
            
            if university_id is None:
                message_label = self.query_one('#professor-form__message-label', Label)
                message_label.update("Please select a university for the professor.")
                return

            new_professor = add_professor(self.__db_session, name, email, university_id, notes)
            add_professor_tags(self.__db_session, new_professor.id, selected_tag_ids)

            name_input.value = ""
            email_input.value = ""
            notes_input.text = ""

            message_label = self.query_one('#professor-form__message-label', Label)  
            message_label.update(f"Professor '{name}' added successfully with {len(selected_tag_ids)} tag(s).") 

            professor_list = self.query_one('#professor-form__professor-list', ListView)
            professor_list.clear()
            for professor in get_professors_by_user(self.__db_session, self.__active_user.id):
                professor_list.append(ListItem(Label(f"{professor.name} @ {professor.university.name}")))


    def on_mount(self):
        self.refresh_tags()
        self.refresh_universities()

    def refresh_tags(self):
        tags_selection = self.query_one('#professor-form__tags-selection', SelectionList)
        tags_selection.clear_options()
        for tag in get_tags_by_user(self.__db_session, self.__active_user.id):
            tags_selection.add_option((tag.name, tag.id))

    def refresh_universities(self):
        university_select = self.query_one('#professor-form__university', Select)

        options = [
            (uni.name, uni.id)
            for uni in get_universities_by_user(self.__db_session, self.__active_user.id)
        ]

        university_select.set_options(options)