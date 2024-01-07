# Importa i moduli necessari
import os
import questionary
import typer

from python_on_whales import docker
from typing_extensions import Annotated

from rich import print
from rich.console import Console
from rich.table import Table

# Importa l'oggetto 'app' dal modulo 'scripts'
from scripts import app

# Commenti di spiegazione per i comandi Docker
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

# Commenti di spiegazione per l'esecuzione dello script da riga di comando
# py ./bin/main.py build --tag docs-python3:latest --static-directory docs-python3 --docker-file web-server.Dockerfile
# py ./bin/main.py build --tag docs-python3:latest --docker-file web-server.Dockerfile

# Definizione del comando 'build' nell'applicazione Typer
@app.command()
def build(
    tag: Annotated[str, typer.Option(help="Tag name of build image, ex: my-name:latest")],
    static_directory: Annotated[str, typer.Option(help="Static file directory name (inside public)")] = '',
    docker_file: Annotated[str, typer.Option(help="Docker file to point", rich_help_panel="Optional Arguments")] = 'docker/web-server.Dockerfile',
):
    # Se la cartella 'public' non esiste, la crea
    if not os.path.exists(os.path.join(os.getcwd(), 'public')):
        os.makedirs(os.path.join(os.getcwd(), 'public'))
        
    # Se il parametro 'static_directory' è vuoto, chiede all'utente di selezionarne uno
    if len(static_directory) == 0:
        static_directory = questionary.select(
            "public",
            os.listdir(os.path.join(os.getcwd(), "public"))
        ).ask()
    
    # Inizializza un oggetto 'Console' per l'output formattato
    console = Console()
    print("[yellow]Building[/yellow] [bold red]" + tag + "[/bold red] [green]from[/green] " + static_directory + "...\n")

    # Esegue il comando Docker 'build' utilizzando il modulo 'python_on_whales'
    result = docker.build(
        context_path=os.getcwd(),
        file=os.path.join(os.getcwd(), 'docker', docker_file),
        tags=tag,
        build_args={'PUBLIC_DIR': './public/'+ static_directory +'/'},
    )
    
    # Crea e stampa una tabella con le informazioni sul tag e la dimensione dell'immagine Docker
    table = Table("Tags", "Size (MB)")
    table.add_row(result._get_inspect_result().repo_tags[0], str(result._get_inspect_result().size/10000)[:2])
    console.print(table)
    print("\n[yellow]Complete ![/yellow] :boom:")
