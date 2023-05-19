#!/usr/bin bash

pip install ruff black isort --upgrade
ruff scripts
black scripts --check
isort scripts --check-only
