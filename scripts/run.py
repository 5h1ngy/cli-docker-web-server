# Importa i moduli necessari
import questionary
import typer

from typing import Annotated
from python_on_whales import DockerException, docker
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

# py ./bin/main.py run --image-tag docs-python3:latest --output-port 8080 --container-name docs-python3

# Definizione del comando 'run' nell'applicazione Typer
@app.command()
def run(
    image_tag: Annotated[str, typer.Option(help="Tag name of build image, ex: my-name:latest")] = '',
    output_port: Annotated[str, typer.Option(help="Port binding value ex: 8080")] = '',
    container_name: Annotated[str, typer.Option(help="Name to assign to container")] = '',
):
    # Titolo e lista delle scelte per le immagini Docker disponibili
    title = f"Images list: "
    choices = []
    
    # Popola la lista delle scelte con i tag delle immagini Docker
    for image in docker.image.list():
        choices.append(image.repo_tags[0])
    
    # Se il parametro 'image_tag' è vuoto, chiede all'utente di selezionarne uno
    if len(image_tag) == 0:
        image_tag: str = questionary.select(title, choices).ask()
    
    # Se il parametro 'output_port' è vuoto, chiede all'utente di inserire un valore
    if len(output_port) == 0:
        output_port = questionary.text(message='Type port binding', default='8080').ask()
    
    # Se il parametro 'container_name' è vuoto, chiede all'utente di inserire un valore
    if len(container_name) == 0:
        container_name = questionary.text(message='Type container name', default=image_tag.split(':')[0]).ask()
    
    try:
        # Esegue il comando Docker 'run' utilizzando il modulo 'python_on_whales'
        result = docker.run(
            image=image_tag,
            detach=True,
            publish=[[output_port,'80']],
            name=container_name,
        )
        print(result)
            
    except DockerException as error:
        # Se si verifica un'eccezione Docker, controlla il codice di ritorno
        if error.return_code == 125:
            # Se il codice di ritorno è 125, prova a riavviare il container
            docker.restart(containers=container_name)
            print('Restart complete ' + container_name)
