#!/bin/bash

# Function to perform a Google search and return the first result URL
google_search() {
  query=$1
  search_url="https://www.google.com/search?q=${query// /+}"
  
  # Perform the search using curl
  response=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" "$search_url")
  
  # Parse the response to find the first result URL
  url=$(echo "$response" | grep -oP 'url\?q=\K(https://[^&]+)' | head -n 1)
  
  echo "$url"
}

# Example query
query="Withington Labour party website"
result_url=$(google_search "$query")

if [ -n "$result_url" ]; then
  echo "First result URL for '$query': $result_url"
else
  echo "No result found for '$query'"
fi
