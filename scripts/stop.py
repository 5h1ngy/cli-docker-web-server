# Importa i moduli necessari
import questionary
import typer

from typing import Annotated
from python_on_whales import docker
from rich import print

# Importa l'oggetto 'app' dal modulo 'scripts'
from scripts import app

# Commenti di spiegazione per i comandi Docker
# docker run \
#     --detach \
#     --publish 8080:80 \
#     --name docs-python3 \
#     docs-python3 

# docker.run(
#     image='docs-python3:latest',
#     detach=True,
#     publish=[['8080','80']],
#     name='docs-python3',
# )

# py ./bin/main.py stop --container-name docs-python3

# Definizione del comando 'stop' nell'applicazione Typer
@app.command()
def stop(
    container_name: Annotated[str, typer.Option(help="Name to assign to container")] = '',
):
    # Titolo e lista delle scelte per i container Docker in esecuzione
    title = f"Running containers: "
    choices = []
    
    # Popola la lista delle scelte con i nomi dei container Docker in esecuzione
    for container in docker.container.list():
        choices.append(container.name)
        
    # Se il parametro 'container_name' è vuoto, chiede all'utente di selezionarne uno
    if len(container_name) == 0:
        container_name = questionary.select(title, choices).ask()
        
    # Esegue il comando Docker 'stop' utilizzando il modulo 'python_on_whales'
    docker.stop(container_name)
    print(container_name + " stopped! :boom:")
