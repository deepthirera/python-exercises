FIRST TIME:
```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -U uv
uv pip install -r pyproject.toml
```

SUBSEQUENT RUNS
source .venv/bin/activate
uv pip install -r pyproject.toml
pytest -s

uv
https://docs.astral.sh/uv/guides/projects/#running-commands

pytest
https://docs.pytest.org/en/stable/getting-started.html#get-started

To run trivia game
export PYTHONPATH="${PYTHONPATH}:path-to-python-learn-folder
Example:
export PYTHONPATH="${PYTHONPATH}:/Users/deepthir/projects/code/python-learn/"
python src/trivia_game/quiz_controller.py
