from TUI.app import ApplyApp

from utils import create_db_connection

def main():
    session_maker = create_db_connection()
    app = ApplyApp(db_session=session_maker())
    app.run()   

if __name__ == "__main__":
    main()