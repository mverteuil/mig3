#!/usr/bin/env bash
set -euo pipefail
export IFS=$"\n\t"


# Install dependencies
yarn install
# Run development server
yarn serve
