#!/bin/bash
pip install --user --upgrade pip
pip install --user -r requirements.txt
python -m nltk.downloader popular
PROJECT=${PWD##*/}
cd ../ && putup $PROJECT --force --no-skeleton -p $PROJECT
cd $PROJECT
pip install --user -e .
mkdir -p data
mkdir -p logs
echo "data/" >> .gitignore