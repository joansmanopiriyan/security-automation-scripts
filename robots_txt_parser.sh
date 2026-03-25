#!/bin/bash

echo "Enter target URL (example: https://example.com)"
read target

robots_url="$target/robots.txt"

echo ""
echo "Checking robots.txt at: $robots_url"
echo ""

response=$(curl -s $robots_url)

if [[ $response == *"User-agent"* ]]; then
    echo "[FOUND] robots.txt exists"
    echo ""
    echo "Discovered paths:"
    echo ""

    echo "$response" | grep -E "Disallow|Allow"

else
    echo "[NOT FOUND] robots.txt not present"
fi
