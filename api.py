import requests
import json

def fetchLibraryData():
    url = "https://openlibrary.org/search.json?author=tolkien"

    try:
        response = requests.get(url , timeout = 5)
        data = response.json()
        # data_str = json.dumps(data)
        return data
    except(requests.exceptions.Timeout):
        print("Request is timed out, try again later!")
        return None
    except:
        print("Something went wrong!")
        return None