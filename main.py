import argparse
from modules.subdomain_enum import enumerate_subdomains
from modules.port_scan import scan_ports
from modules.service_fingerprint import fingerprint_services
from utils.output import save_output

def main():
    parser = argparse.ArgumentParser(description="Automated Recon & Enumeration Framework")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("--output", help="Output file (JSON)", default="result.json")
    args = parser.parse_args()

    print(f"[+] Enumerating subdomains for {args.target}...")
    subdomains = enumerate_subdomains(args.target)
    print(f"[+] Found subdomains: {subdomains}")

    results = {}
    for sub in subdomains:
        print(f"[+] Scanning ports for {sub}...")
        ports = scan_ports(sub)
        print(f"[+] Found open ports: {ports}")

        fingerprints = {}
        for port in ports:
            print(f"[+] Fingerprinting service on {sub}:{port}...")
            fingerprints[port] = fingerprint_services(sub, port)
            print(f"[+] {sub}:{port} => {fingerprints[port]}")
        results[sub] = {"ports": ports, "fingerprints": fingerprints}

    save_output(results, args.output)
    print(f"[+] Results saved to {args.output}")

if __name__ == "__main__":
    main()