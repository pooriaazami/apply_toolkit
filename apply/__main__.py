# import sys

# import typer

# from TUI.app import ApplyApp

# from utils import create_db_connection

# app = typer.Typer()

# @app.command()
# def hello(name: str = 'Pooria'):
#     typer.echo(f'Hello, {name}! This is the apply toolkit app.')

# @app.callback()
# def main():
#     if len(sys.argv) > 1:
#         return
    
#     session_maker = create_db_connection()
#     ApplyApp(db_session=session_maker()).run()

# if __name__ == "__main__":
#     app()

import typer

from TUI.app import ApplyApp
from utils import create_db_connection

app = typer.Typer()

def run_tui():
    session_maker = create_db_connection()
    ApplyApp(db_session=session_maker()).run()


@app.command()
def hello(name: str = "Pooria"):
    typer.echo(f"Hello, {name}! This is the apply toolkit app.")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        run_tui()


if __name__ == "__main__":
    app()