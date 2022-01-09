#!/bin/bash
# takes in a URL, send request to that URL, and displaY size of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
