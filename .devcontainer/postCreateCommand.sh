#!/bin/bash

echo "Installing  node modules"
npm install

echo "Building Interface App"
npm run build

echo "Installing python requirements."
pip3 install --user -r server/requirements.txt

echo "run: cd server"
echo "run: python3 generate.py"
echo "run: python3 server.py"
