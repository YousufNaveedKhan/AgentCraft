import requests

try: 
    response = requests.get("https://jsonplaceholder.typicode.com/posts/invalid_url")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"API call fail hui: {e}")