#!/bin/bash

version=$(google-chrome --version | awk '{print $3}')

echo Your chrome version is $version, installing the driver for this version

curl -O https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip

unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip

echo 'Done!'
