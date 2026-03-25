import requests

# List of websites to check
urls = [
    "https://example.com",
    "https://google.com"
]

# Security headers to verify
security_headers = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def check_headers(url):
    try:
        response = requests.get(url)
        print(f"\nChecking: {url}")

        for header in security_headers:
            if header in response.headers:
                print(f"[+] {header}: Present")
            else:
                print(f"[-] {header}: Missing")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error checking {url}: {e}")


for url in urls:
    check_headers(url)
