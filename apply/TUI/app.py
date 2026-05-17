from textual.app import App
from textual.widgets import Header, Footer

from db.queries import get_number_of_users

from . import LoginScreen, RegisterScreen, MainScreen


class ApplyApp(App):

    TITLE = "Apply Toolkit"

    def __init__(self, db_session=None):
        super().__init__()
        self.__db_session = db_session
        self.__screen = None

    async def on_mount(self) -> None:
        self.run_worker(self.flow(), exclusive=True)

    async def flow(self):
        if self.__screen is None:
            if get_number_of_users(self.__db_session) == 0:
                self.__screen = 'register'
            else:
                self.__screen = 'login'

        while self.__screen != 'exit':
            if isinstance(self.__screen, str):
                if self.__screen == 'register':
                    self.__screen = await self.push_screen_wait(RegisterScreen(db_session=self.__db_session))
                elif self.__screen == 'login':
                    self.__screen = await self.push_screen_wait(LoginScreen(db_session=self.__db_session))
            else:
                self.__screen = await self.push_screen_wait(MainScreen(db_session=self.__db_session, user=self.__screen))

            if self.__screen == 'exit':
                self.exit()
       


    def compose(self):
        yield Header()
        yield Footer()