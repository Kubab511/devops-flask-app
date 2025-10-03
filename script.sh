#!/bin/bash

echo "Updating the machine"
sudo apt update -y && sudo apt upgrade -y

echo "Installing required packages"
sudo apt install -y nano vim python-is-python3 python3-venv python3-pip python3-flask

echo "Creating the virtual environment"
python -m venv .my_venv

echo "Entering the virtual environment"
source .my_venv/bin/activate

echo "Running the file"
flask --app hello run --host=0.0.0.0