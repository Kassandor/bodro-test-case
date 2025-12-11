#!/bin/sh

exec uvicorn main:app --lifespan on --host 0.0.0.0 --port 8000 --reload