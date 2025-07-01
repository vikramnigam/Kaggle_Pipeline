
# This module handles the integration with the Kaggle API.
# It authenticates the user, downloads the dataset, and extracts the contents into a date-specific folder.

import os
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_dataset(dataset_name: str, download_path: str = 'data'):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset=dataset_name,
        path= download_path,
        unzip=True
    )

    return os.listdir(download_path)