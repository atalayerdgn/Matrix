#!/bin/bash
find . -name "__pycache__" -type d -exec rm -r {} +
find . -name "*.pyc" -type f -exec rm {} +
