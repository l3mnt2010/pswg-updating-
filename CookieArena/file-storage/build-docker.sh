#!/bin/bash
docker rm -f path-traversal-002
docker build --tag=path-traversal-002 .
docker run -p 1337:1337 --name=path-traversal-002 path-traversal-002