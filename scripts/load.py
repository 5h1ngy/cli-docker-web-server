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
def load(
    image_name: Annotated[str, typer.Option(help="Image name to save")] = '',
):
    dumpsDir = os.path.join(os.getcwd(), "dumps")
    title = f"Running containers: "
        
    if len(image_name) == 0:
        image_name = questionary.select(title,os.listdir(dumpsDir)).ask()
    
    if not os.path.exists(dumpsDir):
        os.makedirs(dumpsDir)
        
    docker.load(input=os.path.join(os.getcwd(), 'dumps', image_name))
    print(image_name + " load! :boom:")