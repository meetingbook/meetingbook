# Backend

## Prerequisites

- We use Python 3
- Install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html) `pip3 install virtualenv`
- Go to `backend` folder
- Initialise virtualenv using either `venv` or `.venv` folder name: `virtualenv .venv`
- Activate virtualenv: `source .venv/bin/activate`
- Install all dependencies
    ```bash
    pip3 install -r requirements.txt   
    ```

## Getting Started

### Run server

If you want to run a backend API:

1. open a new terminal window
2. go to `backend` folder
3. activate virtual env 
4. run command in terminal or Git bash (optional)
    ```bash
    export PYTHONPATH="$PWD"
    ```
5. run:
    ```bash
    export FLASK_APP=server
    flask run
   
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

## Migration

For working with migrations see the README in folder: `meetingbook/backend/migration/README.md`


## Documentation API

API documentation is available at ```.../api/docs```
For example: 
The server is running locally the path is: ```http://localhost:5000/api/docs/```