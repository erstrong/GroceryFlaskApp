import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'