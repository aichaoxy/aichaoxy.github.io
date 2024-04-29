#!/usr/bin/env bash
set -e
python -m pip install --upgrade pip
pip3 install pdm
pdm install
source .venv/bin/activate
pelican content