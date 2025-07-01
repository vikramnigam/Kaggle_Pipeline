 # **🚀 Simple Data Pipeline with FastAPI, Kaggle API & SQL Server**

##  📌 Project Goal

### The main purpose of this project was to build a basic data pipeline which:

- Fetches data from a source (right now from Kaggle)

- Cleans and prepares it

- And finally saves it into a database.

### Later on, it can be changed based on needs —
### like if we want to get data from a *CRM Tool* or store data on cloud, we can update this pipeline easily.


## 🔧 Tools Used

- FastAPI – To create an API endpoint and trigger the process

- Kaggle API – To fetch the dataset from Kaggle

- Pandas – For data cleaning and merging

- SQLAlchemy – To save final data into MS SQL Server

## 📁 Project Structure

### 📂 kaggle_pipeline
> kaggle_api.py

> service.py

> data_cleaning.py 

> save.py


## 🧠 How It Works

1. You hit the FastAPI endpoint → /run-process

2. It downloads the dataset and saves it in a folder with today’s date

3. Data is merged into one file and cleaned (like fixing column names, formatting month, handling nulls etc.)

4. Then it's pushed to the SQL database


## 🛠️ Notes

- You can replace Kaggle API part with any other data source (like CRM, API, CSV from cloud, etc.)

- You can also change the final database to anything else like MySQL, PostgreSQL, or cloud storage


## ✅ Example Use Case

Let’s say this whole setup is scheduled using something like Airflow to run every morning:

- It will automatically get new data

- Clean and store it

- And your analytics/dashboard will always have updated info

