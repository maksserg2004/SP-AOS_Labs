#!/bin/bash

echo "Counting files in /etc..."

if [ "$EUID" -ne 0 ]; then
    echo "Error: This script must be run as root or with sudo privileges" >&2
    exit 1
fi

if [ ! -d "/etc" ]; then
    echo "Error: Directory /etc does not exist!" >&2
    exit 1
fi

count=$(find /etc -type f 2>/dev/null | wc -l)

if [ $? -ne 0 ]; then
    echo "Error: find command failed" >&2
    exit 1
fi

echo "Number of regular files: $count"
exit 0