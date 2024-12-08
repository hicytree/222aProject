#!/bin/bash

# Define variables
RECEIVER_IP="52.12.185.223"         # Replace with your receiver's IP address
REMOTE_USER="ec2-user"            # Replace with your receiver's SSH user
REMOTE_PATH="/home/ec2-user"  # Destination path on the receiver
LARGE_FILE="largefile"            # The file to transfer
KEY_PATH="serverkey.pem"       # SSH private key path

rm -rf cwnd_log.txt

# Generate a large file if it doesn't exist
# if [ ! -f "$LARGE_FILE" ]; then
#     echo "Generating a large file ($LARGE_FILE)..."
#     fallocate -l 500M "$LARGE_FILE"
# fi

# Monitor congestion window during transfer
echo "Starting transfer and monitoring cwnd..."
(while :; do
    # Use ss to get specific TCP info, filter out unneeded details
    ss -i dst "$RECEIVER_IP" | grep -E 'cwnd' | awk -v now="$(date +%s%3N)" '{ print "time:" now, $0 }' >> cwnd_log.txt
done) &
MONITOR_PID=$!

# Start the file transfer
# scp -i "$KEY_PATH" "$LARGE_FILE" "$REMOTE_USER@$RECEIVER_IP:$REMOTE_PATH"
python3 clientsender.py

# Stop monitoring
kill "$MONITOR_PID"
echo "File transfer complete. Stopping cwnd monitoring."

rm -rf largefile