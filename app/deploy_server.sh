#!/bin/bash
# Script to deploy our Django instance. Calls Apache mod_wsgi_express to start
# its daemon, and populates a clean database instance with example data.
#
# This script will be called by docker-compose.yml from the parent directory.
APP_BASE=/app/
DJANGO_BASE=$APP_BASE/isa_app/

python $DJANGO_BASE/manage.py makemigrations
python $DJANGO_BASE/manage.py migrate
python $DJANGO_BASE/manage.py loaddata $APP_BASE/db.json
mod_wsgi-express start-server --reload-on-changes --log-to-terminal --working-directory $DJANGO_BASE $DJANGO_BASE/isa_app/wsgi.py