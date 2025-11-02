#!/bin/bash

# Path to your Python script
SCRIPT="./tlk_main.py"
cd /home/oleksii/tlk-news/
# Infinite loop to restart script on failure
while true; do
    echo "Starting $SCRIPT..."
    /home/oleksii/bin/python3 "$SCRIPT" >> output.log
    
    echo "Script crashed or exited. Restarting in 5 seconds..."
    sleep 5
done
