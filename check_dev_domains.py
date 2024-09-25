import requests
import itertools
import string
import time

# Function to check domain availability using the specified API
def is_domain_available(domain):
    url = f"https://pubapi-dot-domain-registry.appspot.com/check?domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('available', False)  # Check if the domain is available
    return False

# Generate combinations of letters and digits for the given lengths
def generate_domains(length):
    characters = string.ascii_lowercase + string.digits
    return (''.join(candidate) for candidate in itertools.product(characters, repeat=length))

# Main function to check for available domains
def find_available_domains():
    available_domains = []
    for length in range(1, 6):  # For lengths 1 to 5
        for domain in generate_domains(length):
            full_domain = f"{domain}.dev"
            if is_domain_available(full_domain):
                print(f"Available: {full_domain}")
                available_domains.append(full_domain)
            time.sleep(0.1)  # Sleep to avoid hitting rate limits
    return available_domains

if __name__ == "__main__":
    available_domains = find_available_domains()
    print(f"Total available domains found: {len(available_domains)}")
