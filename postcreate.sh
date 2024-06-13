#!/bin/bash
pip install --user --upgrade pip
pip install --user -r requirements.txt
# pip install -user nuitka  # python -m nuitka --follow-imports program.py https://github.com/Nuitka/Nuitka-Action
python -m nltk.downloader popular
PROJECT=${PWD##*/}
cd ../ && putup $PROJECT --force --no-skeleton -p $PROJECT
cd $PROJECT
pip install --user -e .
mkdir -p data
mkdir -p logs
echo "data/" >> .gitignore