import os

# Paths
this_folder_path = os.path.dirname(__file__)
ROOT_FOLDER_PATH = os.path.join(this_folder_path, '..')
DATA_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, 'data')
NOTEBOOKS_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, 'notebooks')
MODELS_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, 'models')
ARTIFACTS_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, 'artifacts')
CODE_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, 'src')
MLFLOW_TRACKING_URI = os.path.join(ROOT_FOLDER_PATH, 'mlruns')
