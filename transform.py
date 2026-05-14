import pandas as pd
from datetime import datetime
from extract import extract_news

data = extract_news()

def transform_news(data):
    
    cleaned_data = []
    
    for article in data:
        cleaned_data.append(
            {
                "source"       : article.get("source",{}).get("name"),
                "author"       : article.get("author"),
                "title"        : article.get("title"),
                "published_at" : article.get("publishedAt"),
                "inserted_at"  : datetime.now() 
            }
        )
    
    cleaned_df = pd.DataFrame(cleaned_data)

    return cleaned_df

transformed_df = transform_news(data)

print(transformed_df.head())
print(transformed_df)
