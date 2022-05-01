#! /bin/bash
set -euxo pipefail

if [ -a .env ]
then
  echo ".env exists already so not copying from .env.example"
else
  echo ".env not found, so copying from .env.example"
  cp .env.example .env
fi

exec uwsgi --http :80 --workers 1 --threads 2 --wsgi-file givemeadatabase.wsgi --chdir /usr/src/app/givemeadatabase/

