#!/bin/bash
# Change to project directory
cd $1

# Activate virtualenv
source myenv/bin/activate

# Source env variables
source .env

# Execute python process
python src/scripts/execution/pyscripts/execution.py
