#!/bin/bash
set -e

pytest /tests/test_outputs.py \
    --json-report \
    --json-report-file=/tmp/pytest-report.json \
    -rA

echo 1 > /app/reward.txt
