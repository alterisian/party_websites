import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://en.wikipedia.org/wiki/Constituencies_of_the_Parliament_of_the_United_Kingdom"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare to write to CSV
with open('all_uk_constituencies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Constituency", "Country"])  # headers

    # Dictionary to count the constituencies for each country
    constituency_count = {'England': 0, 'Wales': 0, 'Scotland': 0, 'Northern Ireland': 0}
    table_ids = {'England': 'England', 'Wales': 'Wales', 'Scotland': 'Scotland', 'Northern Ireland': 'NI'}

    # Iterate over each country and process the corresponding table
    for country, table_id in table_ids.items():
        table = soup.find('table', id=table_id)
        rows = table.find_all('tr')
        for row in rows[1:]:  # skip the header row
            cells = row.find_all('td')
            if cells:
                constituency = cells[0].text.strip()
                writer.writerow([constituency, country])
                constituency_count[country] += 1  # increment the count for the country

# Check if the numbers are as expected
expected_counts = {'England': 533, 'Wales': 40, 'Scotland': 59, 'Northern Ireland': 18}
if constituency_count == expected_counts:
    print("All constituencies counted correctly.")
else:
    print("There was a mismatch in expected constituency counts:", constituency_count)
