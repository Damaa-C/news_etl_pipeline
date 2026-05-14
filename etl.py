import os
import requests
import pandas as pd

from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

API_KEY = os.getenv("API_KEY")



def news_etl_pipeline():
    """
    Full ETL pipeline with nested functions
    """
    # EXTRACT

    def extract():
        print("Extracting data...")

        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()
        
        articles = data.get("articles", [])
        
        return articles

    # TRANSFORM

    def transform(articles):
        print("Transforming data...")

        cleaned_data = []

        for article in articles:
            cleaned_data.append(
                {
                    "source": article.get("source", {}).get("name"),
                    "author": article.get("author"),
                    "title": article.get("title"),
                    "published_at": article.get("publishedAt"),
                    "inserted_at": datetime.now()
                }
            )


        cleaned_df = pd.DataFrame(cleaned_data)

        return cleaned_df

    # LOAD

    def load(df):
        print("Loading data into PostgreSQL...")

        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        dbname = os.getenv("DB_NAME")

        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}?sslmode=require")

        df.to_sql(name="news",con=engine,if_exists="append",index=False)

        print(f"LOAD SUCCESSFUL: {len(df)} rows inserted")

    # PIPELINE EXECUTION

    print("Starting ETL Pipeline...")

    articles = extract()
    df = transform(articles)
    load(df)

    print("ETL Pipeline Completed Successfully!")


# Run pipeline
if __name__ == "__main__":
    news_etl_pipeline()
