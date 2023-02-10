# Modern Cookiecutter Template for Data Science

_An opinionated project structure for data science work using modern python tools._


### Requirements
-----------
 - Python 3.7+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0
 - git
 - [poetry](https://python-poetry.org/docs/#installation) >= 1.2.0


### To start a new project, run:
------------

    cookiecutter https://github.com/JDechery/cookiecutter_hypermodern_ds


### Changes from Cookiecutter Data Science
------------
- Adjustment of directory structure
- Usage of poetry over pip
- Uses git as VCS
- Includes linting with pylint and testing with pytest
- Pre-installs pre-commit hooks including code formatting black

### The directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make lint`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml   <- Poetry package definition
│
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    └── models         <- Scripts to train models and then use trained models to make
        │                 predictions
        ├── predict_model.py
        └── train_model.py
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    pytest tests
