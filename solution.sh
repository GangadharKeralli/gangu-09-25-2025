#!/bin/bash
# Read number from input.txt
num=$(cat input.txt)

# Check even or odd
if (( num % 2 == 0 )); then
  echo -n "even" > output.txt
else
  echo -n "odd" > output.txt
fi
