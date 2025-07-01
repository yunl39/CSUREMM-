import requests
import pandas as pd
import time

API_TOKEN = ''
BASE_URL = 'https://api.marketaux.com/v1/news/all'

all_articles = []
page = 1
MAX_PAGES = 1000

while page <= MAX_PAGES:
    params = {
        'api_token': API_TOKEN,
        'symbols': 'MSFT',
        'published_after': '2020-12-31',
        'published_before': '2025-06-01',
        'language': 'en',
        'limit': 2500,
        'must_have_entities': 'true',
        'sort': 'published_on',
        'page': page,
    }

    response = requests.get(BASE_URL, params=params)


    data = response.json()
    if 'data' not in data or not data['data']:
        print("No more data found.")
        break

    all_articles.extend(data['data'])
    print(f"Fetched page {page} with {len(data['data'])} articles")
    page += 1
    time.sleep(1)

df = pd.DataFrame(all_articles)
symbol = params['symbols']

df.to_csv(f"/Data/{symbol}_4.csv", index=False)

print(f"Saved a total of {len(df)} articles")