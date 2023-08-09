#!/bin/bash

ngrok http 8000 > /dev/null 2>&1 &
ngrok_pid=$!
echo "PID of ngrok process: $ngrok_pid"

sleep 2  # Wait for ngrok to establish the tunnel (adjust this as needed)

ngrok_url=$(curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

echo "ngrok URL: $ngrok_url"

python3 api.py


