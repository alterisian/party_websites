import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_constituencies(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the appropriate table or content section
    # This will need to be adjusted to the specific structure of the page
    constituencies = []
    for item in soup.find_all('div', {'class': 'div-col'}):  # Adjust the selector based on actual webpage layout
        links = item.find_all('a')
        for link in links:
            constituencies.append(link.text)  # Get the text of the link

    return constituencies

def main():
    url = 'https://en.wikipedia.org/wiki/2023_Periodic_Review_of_Westminster_constituencies'
    constituencies = scrape_constituencies(url)
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(constituencies, columns=['Constituency'])
    
    # Save the DataFrame to a CSV file
    df.to_csv('UK_Constituencies_2024.csv', index=False)
    print("CSV file has been created successfully.")

if __name__ == "__main__":
    main()
