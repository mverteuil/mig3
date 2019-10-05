#!/usr/bin/env bash
set -euo pipefail
export IFS=$"\n\t"

# Generate environment variables if they don't already exist
barb -z
# Collect staticfiles
python mig3/manage.py collectstatic --no-input
# Run migrations
python mig3/manage.py migrate
# Run development server
python mig3/manage.py runserver ${1:-"0:8000"}
