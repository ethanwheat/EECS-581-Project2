# EECS-581 Project 1

This is the repository for Project 1 for KU EECS-581 (Software Engineering II).

## Getting Started

This project requires Python 3.12^

```
python ./main.py
```

## Testing

```
python -m unittest discover -v -s tests
```

### Generate Coverage

Uses [`coverage`](https://pypi.org/project/coverage/), install in your preferred manner. Below is demonstrated with [`pipx`](https://pypi.org/project/pipx/)

```
pipx run coverage run -m unittest discover -v -s tests
pipx run coverage report --show-missing
```

You can also generate a .html file for easier navigation
```
pipx run coverage run -m unittest discover -v -s tests
pipx run coverage html
```

Then open the file `./html_cov/index.html` in your preferred browser