#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi


# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo "pip3 is installed."
else
    echo "pip3 is not installed. Please install pip3."
    exit 1
fi

# Create a virtual environment and install Flask
python3 -m venv .venv
source .venv/bin/activate
pip install Flask

# Run the Flask app
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=8080
