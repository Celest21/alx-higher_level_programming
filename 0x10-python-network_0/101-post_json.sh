#!/bin/bash
# Sends a JSON POST request to the provided URL with the contents of a file as the body of the request
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

