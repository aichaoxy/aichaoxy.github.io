#!/usr/bin/env bash
set -e
pip3 install pdm
pdm install
source .venv/bin/activate
pelican content