import os
import questionary
import typer

from python_on_whales import docker
from typing_extensions import Annotated

from rich import print
from rich.console import Console
from rich.table import Table

from scripts import app

# docker.build(
#     context_path=os.getcwd(),
#     file=os.path.join(os.getcwd(),'docker/web-server.Dockerfile'),
#     tags='docs-python3',
#     build_args={'PUBLIC_DIR': './public/docs-python3/'}
# )

# docker build \
#   --file ./docker/web-server.Dockerfile \
#   --build-arg PUBLIC_DIR=./public/docs-python3/ \
#   --tag docs-python3 \
#   .

# py ./bin/main.py build --tag docs-python3:latest --static-directory docs-python3 --docker-file web-server.Dockerfile

# py ./bin/main.py build --tag docs-python3:latest --docker-file web-server.Dockerfile

@app.command()
def build(
    tag: Annotated[str, typer.Option(help="Tag name of build image, ex: my-name:latest")],
    static_directory: Annotated[str, typer.Option(help="Static file directory name (inside public)")] = '',
    docker_file: Annotated[str, typer.Option(help="Docker file to point", rich_help_panel="Optional Arguments")] = 'docker/web-server.Dockerfile',
):
    if not os.path.exists(os.path.join(os.getcwd(), 'public')):
        os.makedirs(os.path.join(os.getcwd(), 'public'))
        
    if len(static_directory) == 0:
        static_directory = questionary.select(
            "public",
            os.listdir(os.path.join(os.getcwd(), "public"))
        ).ask()
    
    console = Console()
    print("[yellow]Building[/yellow] [bold red]" + tag + "[/bold red] [green]from[/green] " + static_directory + "...\n")

    result = docker.build(
        context_path=os.getcwd(),
        file=os.path.join(os.getcwd(), 'docker', docker_file),
        tags=tag,
        build_args={'PUBLIC_DIR': './public/'+ static_directory +'/'},
    )
    
    table = Table("Tags", "Size (MB)")
    table.add_row(result._get_inspect_result().repo_tags[0], str(result._get_inspect_result().size/10000)[:2])
    console.print(table)
    print("\n[yellow]Complete ![/yellow] :boom:")