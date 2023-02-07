#!/usr/bin/env bash

git init -b main
poetry install
poetry run pre-commit install
git add . && git commit -qm 'initial commit'
