import json
import subprocess
import sys

def load_domains(file_path):
    with open(file_path, 'r') as f:
        domains = json.load(f)
    return domains

def scan_domain(domain):
    try:
        result = subprocess.run(['ping', '-c', '3', domain], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"ALIVE: {domain}")
            return True
    except Exception:
        pass
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py domains.json")
        sys.exit(1)

    domains = load_domains(sys.argv[1])
    for domain in domains:
        scan_domain(domain.strip())
