import requests
from bs4 import BeautifulSoup
import re

# List of party websites by constituency
websites = {
    "Bath": {
        "Labour": "https://www.bathlabour.org.uk",
        "Green": "https://bath.greenparty.org.uk",
        "LibDem": "https://www.bathlibdems.org.uk"
    },
    "Birmingham, Edgbaston": {
        "Labour": "https://www.birmingham-labour.org.uk",
        "Green": "https://birmingham.greenparty.org.uk",
        "LibDem": "https://www.birminghamlibdems.org.uk"
    },
    "Cambridge": {
        "Labour": "https://www.cambridgelabour.org.uk",
        "Green": "https://cambridge.greenparty.org.uk",
        "LibDem": "https://www.cambridgelibdems.org.uk"
    },
    "Cardiff Central": {
        "Labour": "https://www.cardifflabour.org.uk",
        "Green": "https://cardiff.greenparty.org.uk",
        "LibDem": "https://www.cardiffld.org.uk"
    },
    "Glasgow Central": {
        "Labour": "https://www.glasgowlabour.org.uk",
        "Green": "https://glasgow.greenparty.org.uk",
        "LibDem": "https://www.glasgowlibdems.org.uk",
        "SNP": "https://www.glasgowsnp.org"
    },
    "Leeds West": {
        "Labour": "https://www.leedslabour.org.uk",
        "Green": "https://leeds.greenparty.org.uk",
        "LibDem": "https://www.leedslibdems.org.uk"
    },
    "Manchester Central": {
        "Labour": "https://www.manchesterlabour.org.uk",
        "Green": "https://manchester.greenparty.org.uk",
        "LibDem": "https://www.mcrlibdems.uk"
    },
    "Norwich South": {
        "Labour": "https://www.norwichlabour.org.uk",
        "Green": "https://norwich.greenparty.org.uk",
        "LibDem": "https://norwichlibdems.org.uk"
    },
    "Oxford East": {
        "Labour": "https://www.oxfordlabour.org.uk",
        "Green": "https://www.greenoxford.com",
        "LibDem": "https://www.oxonlibdems.uk"
    },
    "Plymouth, Sutton and Devonport": {
        "Labour": "https://www.plymouthlabour.org",
        "Green": "https://plymouth.greenparty.org.uk",
        "LibDem": "https://www.plymouthlibdems.org.uk"
    }
}

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
