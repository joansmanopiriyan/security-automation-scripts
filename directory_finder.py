import requests

target = input("Enter target URL (example: https://example.com): ")

paths = [
    "admin",
    "backup",
    "uploads",
    "test",
    "old",
    "temp",
    "logs"
]

print(f"\nScanning {target} for common exposed directories...\n")

for path in paths:
    url = f"{target}/{path}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[FOUND] {url}")
        else:
            print(f"[NOT FOUND] {url}")
    except requests.exceptions.RequestException:
        print(f"[ERROR] Could not connect to {url}")
