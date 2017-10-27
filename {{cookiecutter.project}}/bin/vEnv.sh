#!/bin/bash

python3 -m venv env

# this is for bash. Activate
# it differently for different shells
#--------------------------------------
source env/bin/activate 

pip3 install --upgrade pip
pip3 install pytest
pip3 install pytest-cov
pip3 install sphinx

# Utilities
pip3 install ipython
pip3 install tqdm

# scientific libraries
pip3 install numpy
pip3 install scipy
pip3 install pandas
pip3 install sklearn

# database stuff
pip3 install psycopg2

# Charting libraries
pip3 install matplotlib
pip3 install seaborn
pip3 install folium

pip3 freeze > requirements.txt

deactivate