import questionary
import typer

from typing import Annotated
from python_on_whales import docker
from rich import print

from scripts import app

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

@app.command()
def stop(
    container_name: Annotated[str, typer.Option(help="Name to assign to container")] = '',
):
    title = f"Running containers: "
    choices = []
    
    for container in docker.container.list():
        choices.append(container.name)
        
    if len(container_name) == 0:
        container_name = questionary.select(title, choices).ask()
        
    docker.stop(container_name)
    print(container_name + " stopped! :boom:")