#!/bin/bash

pip install -t . -r requirements.txt
zip -r upload.zip function.py test.py `cat requirements.txt | awk -F\= '{print $1"*"}' | tr '\n' ' '`