import pandas as pd
import numpy as np
import os
from utils.utils import types

# Folder paths
THIS_FILE_PATH = os.path.dirname(__file__)
ROOT_FOLDER_PATH = os.path.join(THIS_FILE_PATH, '..')
DATA_FOLDER_NAME = os.path.join('data', 'sources')
DATA_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, DATA_FOLDER_NAME)

# Create paths for every csv file to concatenate
file_paths = []
file_paths.append(os.path.join(DATA_FOLDER_PATH, '221206COVID19MEXICO.csv')) # Dataset up to December 6th, 2022
file_paths.append(os.path.join(DATA_FOLDER_PATH, 'COVID19MEXICO2021.csv')) # Dataset for 2021
file_paths.append(os.path.join(DATA_FOLDER_PATH, 'COVID19MEXICO2020.csv')) # Dataset for 2020
print(f'Data Folder Path is: {DATA_FOLDER_PATH}')

# Load data from individual files
print('Reading individual csv files')
dfs = []
for filepath in file_paths:
    dfs.append(pd.read_csv(filepath, encoding='latin', dtype=types))

# Concatenate them into a single DataFrame
print('Concatenating DataFrames')
df = pd.concat(dfs, axis='index', ignore_index=True)

# Free space used by individual DataFrames
del dfs

# Save the resulting DataFrame
print('Saving resulting DataFrame')
DATASET_PATH = os.path.join(DATA_FOLDER_PATH, 'COVID19MEXICO.csv')
df.to_csv(DATASET_PATH, index=False)
