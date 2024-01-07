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

# Definizione del comando 'load' nell'applicazione Typer
@app.command()
def load(
    image_name: Annotated[str, typer.Option(help="Image name to save")] = '',
):
    # Definisci la directory 'dumps'
    dumpsDir = os.path.join(os.getcwd(), "dumps")
    title = f"Running containers: "
        
    # Se il parametro 'image_name' è vuoto, chiede all'utente di selezionarne uno
    if len(image_name) == 0:
        image_name = questionary.select(title, os.listdir(dumpsDir)).ask()
    
    # Se la directory 'dumps' non esiste, la crea
    if not os.path.exists(dumpsDir):
        os.makedirs(dumpsDir)
        
    # Esegue il comando Docker 'load' utilizzando il modulo 'python_on_whales'
    docker.load(input=os.path.join(os.getcwd(), 'dumps', image_name))
    print(image_name + " load! :boom:")
