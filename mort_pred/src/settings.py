import os

# Paths
this_folder_path = os.path.dirname(__file__)
PRJ_ROOT_FOLDER_PATH = os.path.join(this_folder_path, '..')
PRJ_DATA_FOLDER_PATH = os.path.join(PRJ_ROOT_FOLDER_PATH, 'data')
PRJ_NOTEBOOKS_FOLDER_PATH = os.path.join(PRJ_ROOT_FOLDER_PATH, 'notebooks')
PRJ_MODELS_FOLDER_PATH = os.path.join(PRJ_ROOT_FOLDER_PATH, 'models')
PRJ_ARTIFACTS_FOLDER_PATH = os.path.join(PRJ_ROOT_FOLDER_PATH, 'artifacts')
PRJ_CODE_FOLDER_PATH = os.path.join(PRJ_ROOT_FOLDER_PATH, 'src')
GLOBAL_MLFLOW_TRACKING_URI = os.path.join(PRJ_ROOT_FOLDER_PATH, '..', 'mlruns')
