import psycopg2
from sqlalchemy import create_engine
from transform import transform_news
from  extract import extract_news
from dotenv import load_dotenv
import os

load_dotenv()

data = extract_news()

transformed_df = transform_news(data)

def load_to_postgres(transformed_df):

    user     = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host     =  os.getenv("DB_HOST")
    port     =  os.getenv("DB_PORT")
    dbname   = os.getenv("DB_NAME")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}?sslmode=require')

    transformed_df.to_sql(name="news",con=engine, if_exists="append",index=False)

    print(f"LOAD SUCCESSFUL: {len(transformed_df)} rows added to DB")


load_to_postgres(transformed_df)

