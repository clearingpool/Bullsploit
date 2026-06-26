#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "$1" ]; then
    echo -e "\033[31m[!] Error! Uncorrect path \033[0m"
    echo "Example: $0 Modules/payloads/reversehttp.py"
    exit 1
fi

FULLPATH="${DIR}/$1"

if [ ! -f "$FULLPATH" ]; then
    echo -e "\033[31m[!] Error! File not found on the path: $FULLPATH\033[0m"
    exit 1
fi

HASH=$(sha256sum "$FULLPATH" | awk '{print $1}')
echo -e "\033[32m[+] File:\033[0m $1"
echo -e "\033[36m[+] SHA-256:\033[0m $HASH"
