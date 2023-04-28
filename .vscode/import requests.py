import requests
import json

def search_candidates(api_key, cx_id, query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx_id,
        'q': query,
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    api_key = 'AIzaSyASsLqZrKVvXqpKIeFxGfH2FoZ7dM4dORk'
    cx_id = 'YOUR_CX_ID'

    # Modify the search keywords as needed
    search_keywords = [
        'satellite communication',
        'aerospace engineering',
        'RF engineering',
        'Project Kuiper',
        'LEO satellites',
    ]

    for keyword in search_keywords:
        query = f'{keyword} resume filetype:pdf "seeking employment"'
        print(f'Searching for: {query}')
        results = search_candidates(api_key, cx_id, query)

        if 'items' in results:
            for item in results['items']:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print()
        else:
            print("No results found")

if __name__ == '__main__':
    main()
