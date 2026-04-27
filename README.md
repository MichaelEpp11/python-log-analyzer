# Python Log Analyzer

## Overview
This project analyzes SSH logs and detects suspicious login activity.

## Features
- Reads SSH log data
- Detects failed login attempts
- Counts failed attempts by IP address
- Flags possible brute-force attacks

## Tools Used
- Python
- Linux terminal

## Detection Logic
Any IP address with 3 or more failed login attempts is flagged as a potential brute-force attacker.

## Example Finding
192.168.1.10 was flagged after 3 failed login attempts.

## What I Learned
- How to parse log files with Python
- How brute-force detection works
- How security automation can support incident detection
## Example Output
![Log Analyzer Output](screenshot.png)
