import os

import typer

from TUI.app import ApplyApp
from utils import create_db_connection
from installer import main as install_applytoolkit

app = typer.Typer()

def run_tui():
    session_maker = create_db_connection()
    ApplyApp(db_session=session_maker()).run()


@app.command()
def hello(name: str = "Pooria"):
    typer.echo(f"Hello, {name}! This is the apply toolkit app.")

@app.command()
def install():
    install_applytoolkit()

    os.system('uv run alembic upgrade head')
    

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        run_tui()


if __name__ == "__main__":
    app()