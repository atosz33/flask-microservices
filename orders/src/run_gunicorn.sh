#!/bin/sh
gunicorn --workers 2 --bind :5001 -m 007 wsgi:app

#if you want to use nginx, then change --bind <ip><port> to --bind unix:<app-name>.sock
