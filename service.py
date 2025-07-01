
# This FastAPI app has an endpoint that starts the Kaggle data pipeline.
# When called, it creates a folder with today’s date and downloads the dataset using the Kaggle API.



from datetime import datetime
import os
from fastapi import FastAPI
from kaggle_api import download_kaggle_dataset


app = FastAPI()

@app.get("/run-process")
def run_pipeline():
    dataset_name = 'alphajuliet/au-dom-traffic'
    today = datetime.today().strftime('%Y-%m-%d')
    download_path = os.path.join('data', today)

    files = download_kaggle_dataset(dataset_name, download_path)


    return {
        'message': f'{len(files)} files downloaded successfully',
        'files' : files
    }