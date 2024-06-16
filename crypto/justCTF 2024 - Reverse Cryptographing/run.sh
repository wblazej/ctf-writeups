#!/bin/bash

docker build -t reverse_cryptographing .
docker run --privileged -e FLAG=test -it -p1337:1337 -d reverse_cryptographing
