import requests
import json

def fetch_api_json (url, file_path):
    try:
        #set GET request to API

        response = requests.get(url)
        response.raise_for_status() #raises error for bad status codes
        #parse response json
        data = response.json()
        #write json to an output file

        with open (file_path, "w") as file:
            json.dump(data, file, indent=3) #indent 4 is more standardized
        
        print (f"Data successfully saved to {file_path}")

    except requests.exceptions.RequestException as e:
        print (f"Unknown error {e}")

# Public API endpoint (CoinDesk API for current Bitcoin price)
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
file_path = input("Please enter output file path")
fetch_api_json(url=url, file_path=file_path)
