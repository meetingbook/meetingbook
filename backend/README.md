# Backend

## Code linting

We use [Flake8](https://flake8.pycqa.org/en/2.5.5/index.html) for code linting.

Linting of the code will be running like the part of GitHub Action Workflow.

In order to autoformat your code you can use `bin/auto_format.py`.

## Tests

In order to run tests:
1. go to the `backend` folder
2. run command
```bash
export PYTHONPATH=<path to directory>/meetingbook/backend
```
3. run pytest
```bash
python3 -m pytest
```

## Run server

From `backend` run:

```bash
python server/app.py
```