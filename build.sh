#!/usr/bin/env bash
set -xe
python -m pip install --upgrade pip
pip3 install pdm
pdm install
source .venv/bin/activate
pelican content