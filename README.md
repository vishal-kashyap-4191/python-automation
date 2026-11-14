# Python Automation

Small Python scripts for Linux automation, written while learning Python.

## sitecheck.py

Checks websites listed in `sites.txt` over HTTP and reports UP or DOWN for each one.

- **UP**: the site answers with an HTTP status below 400
- **DOWN (HTTP 404)**: the server answers with an error status
- **DOWN (could not connect)**: DNS failure, timeout or refused connection
- Exit code `0` if every site is up, `1` if any site is down, `2` if `sites.txt` is missing
- `sites.txt` includes two intentionally broken entries (`elo.invalid` and a non-existent GitHub page) to show both failure types
## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python sitecheck.py
```
