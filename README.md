# News ETL Pipeline

## Project Overview

The News ETL Pipeline is a Python-based data engineering project that extracts news headlines from the NewsAPI, transforms the data into a structured format using Pandas, and loads the cleaned data into a PostgreSQL database.

This project demonstrates the core ETL (Extract, Transform, Load) process commonly used in data engineering workflows.

---

# ETL Workflow

## 1. Extract ([extract.py](https://github.com/Damaa-C/news_etl_pipeline/blob/main/extract.py))
The pipeline extracts top news headlines from the NewsAPI using HTTP requests.

### API Endpoint
```python
https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY
```

### Tools Used
- requests
- python-dotenv

---

## 2. Transform ([transform.py](https://github.com/Damaa-C/news_etl_pipeline/blob/main/transform.py))
The extracted JSON data is cleaned and transformed into a Pandas DataFrame.

### Transformed Fields
- source
- author
- title
- description
- published_at
- inserted_at

### Tools Used
- pandas
- datetime

---

## 3. Load ([load.py](https://github.com/Damaa-C/news_etl_pipeline/blob/main/load.py))
The transformed data is loaded into a PostgreSQL database using SQLAlchemy.

### Database
- PostgreSQL

### Tools Used
- sqlalchemy
- psycopg2

---

# Project Structure

```bash
news_etl/
│
├── etl.py
├── testing.ipynb
├── .env
├── requirements.txt
└── README.md
```

---

# Jupyter Notebook Testing

The project uses a Jupyter Notebook (`testing.ipynb`) for:
- testing API extraction
- validating transformed data
- checking PostgreSQL connections
- debugging ETL stages before production execution

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
testing.ipynb
```

---

# Environment Variables

Create a `.env` file in the project root directory:

```env
API_KEY=your_news_api_key

DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository_url>
cd news_etl
```

---

## 2. Create Virtual Environment

```bash
python -m venv data_env
```

Activate environment:

### Linux / WSL
```bash
source data_env/bin/activate
```

### Windows
```bash
data_env\Scripts\activate
```

---

## 3. Install Dependencies 

```bash
pip install -r requirements.txt
```

---

# Required Packages

```txt
pandas
requests
sqlalchemy
psycopg2-binary
python-dotenv
jupyter
notebook
```

---

# PostgreSQL Table Schema

```sql
CREATE TABLE news (
    source TEXT,
    author TEXT,
    title TEXT,
    description TEXT,
    published_at TIMESTAMP,
    inserted_at TIMESTAMP
);
```

---

# Running the Pipeline

Run the ETL pipeline using:

```bash
python etl.py
```

---

# Sample Output

```bash
Starting ETL Pipeline...
Extracting data...
Transforming data...
Loading data into PostgreSQL...
LOAD SUCCESSFUL: 20 rows inserted
ETL Pipeline Completed Successfully!
```

---

# Features

- Extracts real-time news headlines
- Cleans and structures raw JSON data
- Loads data into PostgreSQL
- Uses environment variables for security
- Supports Jupyter Notebook testing
- Monolith ETL workflow with nested ETL stages

---

# Future Improvements

- Add logging system
- Add retry mechanism for failed API requests
- Prevent duplicate inserts
- Schedule pipeline using Apache Airflow
- Dockerize the pipeline
- Add data validation checks

---

