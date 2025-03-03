import requests

def fetch_data(api_url):
    """Fetches JSON data from the given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def filter_and_sort_data(data, filter_key, filter_value, sort_key):
    """Filters the data by a key-value pair and sorts it by another key."""
    filtered_data = [item for item in data if str(item.get(filter_key, "")) == filter_value]
    sorted_data = sorted(filtered_data, key=lambda x: x.get(sort_key, ""))
    return sorted_data

# Example usage:
API_URL = "https://jsonplaceholder.typicode.com/posts"  # Example API (dummy posts)
data = fetch_data(API_URL)

if data:
    filtered_sorted_data = filter_and_sort_data(data, filter_key="userId", filter_value="1", sort_key="id")

    # Print processed data
    for item in filtered_sorted_data:
        print(f"ID: {item['id']}, Title: {item['title']}")

