#!/bin/bash
set -e
cd ./sub || { echo "Failed to enter ./sub directory"; exit 1; }
kaggle k push || { echo "Kaggle push failed"; exit 1; }
cd - > /dev/null  # Return to the previous directory
