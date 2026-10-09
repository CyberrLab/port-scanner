
# Python TCP Port Scanner

A beginner-friendly Python networking project that checks a predefined
list of TCP ports on the local computer.

## Features

- Checks TCP connection availability
- Uses socket programming
- Applies a connection timeout
- Reports ports as open or closed/filtered
- Displays scan time and a final summary

## Requirements

- Python 3.10 or later
- No third-party packages required

## How to Run

Open a terminal in the project directory and execute:

```bash
python port_scanner.py
```

The current version scans `127.0.0.1`, which refers to the local computer.

## Technologies

- Python
- `socket`
- `datetime`

## Learning Outcomes

- TCP networking fundamentals
- Port and service discovery
- Socket programming
- Connection timeouts
- Basic network security concepts

## Limitations

This version scans a fixed list of ports on the local computer.
A port reported as closed or filtered may simply be unavailable or
not accepting connections at the time of the scan.

## Status

Initial version implemented and tested locally on Windows.

## Author

CyberrLab
