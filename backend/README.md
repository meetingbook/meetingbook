# Backend

## Prerequisites

- We use Python 3
- Install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html) using 
either `venv` or `.venv` folder name.
- Go to `backend` folder Install all dependencies
    ```bash
    pip3 install -r requirements.txt   
    ```

## Getting Started

### Run server

If you want to run a backend API:

1. open a new terminal window
2. go to `backend` folder
3. activate virtual env
4. run:
    ```bash
    python server/app.py
    ```

### Run CLI command

If you are an administrator you might want to run a CLI tool:

1. open a new terminal window
2. go to `backend` folder
3. activate virtual env
4. run:
    ```bash
    python -m cli
    ```

## Code linting

We use [Flake8](https://flake8.pycqa.org/en/2.5.5/index.html) for code linting.

Linting of the code will be running like the part of GitHub Action Workflow.

If you want to lint the code locally run:
```bash
flake8 .
```

In order to autoformat your code you can use `bin/auto_format.py`.

## Tests

In order to run tests:
1. go to the `backend` folder
2. run command in terminal or Git bash (optional)
    ```bash
    export PYTHONPATH="$PWD"
    ```
3. run pytest
    ```bash
    python -m pytest
    ```

