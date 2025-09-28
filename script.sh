#!/bin/bash
echo "Підрахунок файлів у /etc..."

count=$(find /etc -type f 2>/dev/null | wc -l)

echo "Кількість файлів: $count"