# Domain Alive Scanner (DAS)

Simple Python util for red team ops. Checks if domains from a JSON list are alive via ICMP ping.

## Features

- Reads domain list from JSON file
- Outputs responsive hosts
- Minimal deps, no external libs

## Usage

```bash
python3 main.py domains.json
```

## Input Format

JSON array of domain strings:

```json
["domain1.com", "domain2.com"]
```

## Notes

- Designed for recon/footprinting
- No stealth features, basic detection avoidance
- Extendable for custom probes
