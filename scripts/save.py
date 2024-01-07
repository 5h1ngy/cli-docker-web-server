import os
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
def save(
    image_name: Annotated[str, typer.Option(help="Image name to save")] = '',
):
    title = f"Images list: "
    choices = []
    
    for image in docker.image.list():
        choices.append(image.repo_tags[0])
        
    if len(image_name) == 0:
        image_name = questionary.select(title, choices).ask()
    
    if not os.path.exists(os.path.join(os.getcwd(), 'dumps')):
        os.makedirs(os.path.join(os.getcwd(), 'dumps'))
        
    docker.save(image_name, output=os.path.join(os.getcwd(), 'dumps', image_name.replace(":", "_") + '.tar.gz'))
    print(image_name + " saved! :boom:")