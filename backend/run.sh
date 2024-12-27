#!/bin/bash
export $(cat .env | xargs)
python run.py 