#!/bin/bash
#!/bin/bash
# To be executed at root project
# Install venv
python3 -m pip install virtualenv
# Create venv
python3 -m virtualenv myenv
# Activate
source myenv/bin/activate
# Install requirements
pip install -r setup/requirements.txt
# Source the environmental files
source .env
