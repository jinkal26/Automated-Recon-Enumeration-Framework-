import requests

def enumerate_subdomains(domain):
    # Simple example using crt.sh for public cert transparency
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        if not r.ok:
            return [domain]
        data = r.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    if domain in sub:
                        subdomains.add(sub.strip())
        return list(subdomains)
    except Exception as e:
        print(f"Error during subdomain enumeration: {e}")
        return [domain]