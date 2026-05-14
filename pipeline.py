from dotenv import load_dotenv
from extract import extract_news
from transform import transform_news
from load import load_to_postgres

load_dotenv()

def news_etl():
    print("--- Starting Tesla News ETL Pipeline ---")

    try:
        # 1. EXTRACT
        print("Step 1: Extracting data from NewsAPI...")
        raw_data = extract_news()
        print(f"Successfully retrieved {len(raw_data)} articles.")

        # 2. TRANSFORM
        print("Step 2: Transforming data into DataFrame...")
        
        transformed_df = transform_news(raw_data) 
        
        if transformed_df.empty:
            print("No data found to transform. Exiting.")
            return

        # 3. LOAD
        print("Step 3: Loading data into PostgreSQL...")
        load_to_postgres(transformed_df)
        
        print("--- ETL Pipeline Completed Successfully ---")

    except Exception as e:
        print(f"!!! ETL Pipeline Failed: {e}")

if __name__ == "__main__":
    news_etl()
