#!/bin/bash
payload=$(python3 ./hex.py)
xxd ~/tmp/output | sed -e "s/40:.*/40:\ $payload/" | xxd -r| tee output
