#!/bin/bash
set -ex
. venv/bin/activate
export FLASK_APP=src/givemeadatabase
export FLASK_DEBUG=1
flask run
