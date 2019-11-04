#!/bin/bash

source /home/protected/venv/bin/activate
gunicorn sassi.wsgi
