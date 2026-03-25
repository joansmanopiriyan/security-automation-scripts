#!/bin/bash

echo "Enter target URL (example: https://example.com)"
read target

echo ""
echo "Checking security headers for: $target"
echo ""

headers=$(curl -s -I $target)

check_header() {
    header_name=$1
    if echo "$headers" | grep -i "$header_name" > /dev/null
    then
        echo "[+] $header_name is present"
    else
        echo "[-] $header_name is missing"
    fi
}

check_header "X-Frame-Options"
check_header "Content-Security-Policy"
check_header "Strict-Transport-Security"
check_header "X-Content-Type-Options"
check_header "Referrer-Policy"
