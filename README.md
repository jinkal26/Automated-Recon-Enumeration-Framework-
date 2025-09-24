# Automated Recon & Enumeration Framework

A Python tool that combines subdomain enumeration, port scanning, and service fingerprinting for automated reconnaissance.

## Features
- Subdomain enumeration via certificate transparency
- Port scanning for common ports
- Service fingerprinting (banner grabbing)

## Usage

```bash
python main.py example.com --output results.json
```

## Extensibility
- Add modules for DNS brute-forcing, more ports, or deeper service fingerprinting.
- Customize output formats.

## Installation

```bash
pip install -r requirements.txt
```