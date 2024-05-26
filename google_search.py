from googlesearch import search

# Function to perform a Google search and return the first result URL
def google_search(query):
    try:
        # Perform the search and convert the generator to a list
        search_results = list(search(query, num_results=1))
        
        # Return the first result
        return search_results[0] if search_results else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example query
query = "Withington Labour party website"
result_url = google_search(query)

if result_url:
    print(f"First result URL for '{query}': {result_url}")
else:
    print(f"No result found for '{query}'")
