#!/bin/bash
# Script sends a JSON POST request to a specified URL and displays the response body

# Check if correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Extract arguments
URL="$1"
JSON_FILE="$2"

# Check if the JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' not found"
    exit 1
fi

# Send POST request with curl, passing the file content as the request body
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"

