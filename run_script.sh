#!/bin/bash

# Path to your Python script
SCRIPT="./tlk_main.py"

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

# Infinite loop to restart script on failure
while true; do
    echo "Starting from $SCRIPT_DIR $SCRIPT..."
    /home/oleksii/bin/python3 "$SCRIPT" >> output.log
    
    echo "Script crashed or exited. Restarting in 5 seconds..."
    sleep 5
done
