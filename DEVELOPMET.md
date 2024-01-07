# Development

To work on this project, it is necessary to have the Linux bash shell on Linux.

## Initialize Virtual Environment

```bash
py -m venv .venv
```

## Install Pip Inside Virtual Environment

```bash
py -m pip install --upgrade pip
py -m pip --version
```

## Activate Virtual Environment (Windows Bash)

```bash
source .venv/Scripts/activate
which python
```

## Utilities

### Add Dependencies

```bash
py -m pip install
```

### Install Requirements

```bash
py -m pip install -r requirements.txt
```

#### Export

```bash
py -m pip freeze
```

## Usage

Ensure the virtual environment is activated before running the application.

```bash
source .venv/Scripts/activate
python main.py ./ path/to/start/directory
```
