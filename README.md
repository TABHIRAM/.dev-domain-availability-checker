# Domain Availability Checker

A simple Python script to check the availability of `.dev` domains using an API. The script generates combinations of letters and digits and checks their availability.

## Features

- Checks domain availability for `.dev` domains.
- Generates available domain names of lengths 1 to 5 using letters and digits. (You can change as per your requirement) 
- Avoids hitting rate limits with a delay between requests.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
   ```bash
   git clone (https://github.com/TABHIRAM/.dev-domain-availability-checker.git)
   cd domain-availability-checker

## API Source

The API used to check domain availability was discovered through the browser's developer tools (Inspect Element) on the website [get.dev](https://get.dev/#get-started). 

Please note that this API is subject to change by the provider (Google), and as such, the functionality of this script may be affected if the API endpoints are modified in the future.
![image](https://github.com/user-attachments/assets/4ffc28ce-8b7a-49e4-a30a-94dd50b5b3c3)

## Disclaimer

This project is intended for educational purposes only. It is not intended to harm or interfere with Google or any other entity. Please use responsibly and in compliance with all applicable laws and guidelines.

