import requests
from bs4 import BeautifulSoup
import re

# Function to scrape emails from a given URL
def scrape_emails(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
        
        # Check for additional contact pages
        contact_links = soup.find_all('a', href=True)
        for link in contact_links:
            if 'contact' in link['href']:
                contact_url = link['href']
                if not contact_url.startswith('http'):
                    contact_url = url + contact_url
                response = requests.get(contact_url)
                contact_soup = BeautifulSoup(response.text, 'html.parser')
                emails.update(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", contact_soup.text))
                
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return set()

# Read websites from the file
websites = {}
file_path = 'websites_queue.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    parts = line.split(', ')
    if len(parts) == 3:
        area, party, url = parts
    elif len(parts) == 4:
        area = f"{parts[0]}, {parts[1]}"
        party = parts[2]
        url = parts[3]
    
    if area not in websites:
        websites[area] = {}
    websites[area][party] = url

# Scraping emails from all listed websites
all_emails = {}
for constituency, parties in websites.items():
    all_emails[constituency] = {}
    for party, url in parties.items():
        emails = scrape_emails(url)
        all_emails[constituency][party] = emails
        print(f"Emails found for {party} in {constituency}: {emails}")

# Optional: Save the results to a file
with open('emails.txt', 'w') as f:
    for constituency, parties in all_emails.items():
        f.write(f"{constituency}:\n")
        for party, emails in parties.items():
            f.write(f"  {party}:\n")
            for email in emails:
                f.write(f"    {email}\n")
        f.write("\n")

print("Scraping completed. Results saved to emails.txt.")
