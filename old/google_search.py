import requests
from bs4 import BeautifulSoup

# Function to search Google and return the first result URL
def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links in the search results
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        if "url?q=" in href and not href.startswith('/url?esrc='):
            url = href.split("url?q=")[1].split("&sa=U")[0]
            return url

    return None

# Example query
query = "Withington Labour party website"
result_url = google_search(query)

if result_url:
    print(f"First result URL for '{query}': {result_url}")
else:
    print(f"No result found for '{query}'")
