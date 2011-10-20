#!/usr/bin/env bash

set -e

test -f selenium-server-standalone-2.8.0.jar || (echo "Downloading Selenium standalone server" && curl -o selenium-server-standalone-2.8.0.jar 'https://selenium.googlecode.com/files/selenium-server-standalone-2.8.0.jar')

java -jar selenium-server-standalone-2.8.0.jar
