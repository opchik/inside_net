#!/bin/bash

source venv/bin/activate
uvicorn src.main:app --reload
# uvicorn src.main:app --host 0.0.0.0 --port 8081
