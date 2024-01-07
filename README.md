# CLI Docker Web Server

This project is a Python Command Line Interface (CLI) for managing a Docker web server. It uses the Typer library to define commands and interacts with Docker through the python_on_whales module.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the CLI, use the following command:

```bash
python main.py
```

Make sure you are in the project's main directory.

## Available Commands

### `build`

```bash
python main.py build --tag [TAG] --static-directory [DIR] --docker-file [DOCKERFILE]
```

This command builds a Docker image using a specific Dockerfile. You can specify the image tag, static directory, and Docker file.

### `run`

```bash
python main.py run --image-tag [TAG] --output-port [PORT] --container-name [NAME]
```

This command starts a Docker container using a specific image. You can specify the image tag, output port, and container name.

### `save`

```bash
python main.py save --image-name [NAME]
```

This command saves a Docker image to a compressed file.

### `load`

```bash
python main.py load --image-name [NAME]
```

This command loads a Docker image from a compressed file.

### `stop`

```bash
python main.py stop --container-name [NAME]
```

This command stops a running Docker container.

## Contributing

If you'd like to contribute to this project, fork the repository and submit a pull request. We welcome contributions.

## License

This project is distributed under the [MIT License](LICENSE).

Feel free to customize the README.md with the specific details of your project, and make sure to add any additional sections or information as needed.
