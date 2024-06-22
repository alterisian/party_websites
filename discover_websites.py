from googlesearch import search
import pandas as pd
import time

# Function to search Google and return the first result URL
def google_search(query, retries=5, backoff_factor=1, initial_sleep=1):
    sleep_time = initial_sleep
    for attempt in range(retries):
        try:
            # Perform the search and convert the generator to a list
            search_results = list(search(query, num_results=1))
            
            # Return the first result
            return search_results[0] if search_results else None
        except Exception as e:
            if "429" in str(e):
                wait_time = sleep_time * (2 ** attempt)
                print(f"Too many requests. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                if attempt == retries - 1:  # If it's the last retry
                    sleep_time = 2  # Increase default sleep time to 2 seconds for future requests
            else:
                print(f"An error occurred: {e}")
                break
    return None

# Function to find party websites for a given constituency
def find_party_websites(constituency, default_sleep=1):
    party_websites = {}
    parties = {"Labour": "Labour", "Green": "Green Party", "LibDem": "Liberal Democrats"}
    
    for party_short, party_full in parties.items():
        query = f"{constituency} {party_full} website"
        print(f"  Searching for {party_full} website...")
        url = google_search(query, initial_sleep=default_sleep)
        if url:
            party_websites[party_short] = url
            print(f"    Found {party_full} website: {url}")
        else:
            print(f"    No {party_full} website found.")
            with open('no_websites.txt', 'a') as no_web_file:
                no_web_file.write(f"{constituency}, {party_full}\n")
        time.sleep(default_sleep)  # Default delay between requests

    return party_websites

# Load the list of all constituencies
file_path = 'all_uk_constituencies.csv'
constituencies_df = pd.read_csv(file_path)

# Print the column names to debug the KeyError issue
print("Column names in the CSV file:", constituencies_df.columns)

# Read the existing searched constituencies from the file
searched_constituencies_file = 'searched_constituencies.txt'
try:
    with open(searched_constituencies_file, 'r') as file:
        searched_constituencies = {line.strip() for line in file.readlines()}
except FileNotFoundError:
    searched_constituencies = set()

# Count entries in searched_constituencies and websites_queue
num_searched = len(searched_constituencies)
num_in_queue = len(constituencies_df) - num_searched

print(f"Number of constituencies in queue: {num_in_queue}")
print(f"Number of constituencies already searched: {num_searched}")

# Get the next 10 constituencies that have not been searched yet
next_constituencies = [c for c in constituencies_df['Constituency'] if c not in searched_constituencies][:4]

# Find and log party websites for the next 10 constituencies
websites = {}
default_sleep = 1  # Initialize default sleep time
for constituency in next_constituencies:
    print(f"Searching websites for: {constituency}")
    websites[constituency] = find_party_websites(constituency, default_sleep=default_sleep)
    default_sleep = 2  # Increase default sleep time to 2 seconds for the next batch

# Update websites_queue.txt with found websites
with open('websites_queue.txt', 'a') as file:
    for constituency, party_urls in websites.items():
        for party, url in party_urls.items():
            file.write(f"{constituency}, {party}, {url}\n")

# Log the searched constituencies
with open('searched_constituencies.txt', 'a') as file:
    for constituency in next_constituencies:
        file.write(f"{constituency}\n")

print("Finished updating websites_queue.txt and searched_constituencies.txt with the next batch of constituencies.")
