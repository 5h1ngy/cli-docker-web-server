# Importa i moduli necessari
import os
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

# Definizione del comando 'save' nell'applicazione Typer
@app.command()
def save(
    image_name: Annotated[str, typer.Option(help="Image name to save")] = '',
):
    # Titolo e lista delle scelte per le immagini Docker disponibili
    title = f"Images list: "
    choices = []
    
    # Popola la lista delle scelte con i tag delle immagini Docker
    for image in docker.image.list():
        choices.append(image.repo_tags[0])
        
    # Se il parametro 'image_name' è vuoto, chiede all'utente di selezionarne uno
    if len(image_name) == 0:
        image_name = questionary.select(title, choices).ask()
    
    # Se la directory 'dumps' non esiste, la crea
    if not os.path.exists(os.path.join(os.getcwd(), 'dumps')):
        os.makedirs(os.path.join(os.getcwd(), 'dumps'))
        
    # Esegue il comando Docker 'save' utilizzando il modulo 'python_on_whales'
    docker.save(image_name, output=os.path.join(os.getcwd(), 'dumps', image_name.replace(":", "_") + '.tar.gz'))
    print(image_name + " saved! :boom:")
