#!/bin/bash

# Upgrade pip to avoid issues
pip install --upgrade pip  

# Ensure all dependencies are installed
pip install -r requirements.txt  

# Debugging step: Print installed packages
pip freeze  

# Run Django static file collection
python3 manage.py collectstatic --noinput  
