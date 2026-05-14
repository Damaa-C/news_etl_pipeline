import requests
from  dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def extract_news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    articles = data.get("articles",[])

    return articles

data = extract_news()

print(data)
