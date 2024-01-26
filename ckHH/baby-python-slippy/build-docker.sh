#!/bin/bash
docker rm -f baby-python-slippy
docker build --tag=baby-python-slippy .
docker run -p 1337:1337 --rm --name=baby-python-slippy baby-python-slippy