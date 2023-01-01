import os
import sys

# Import libraries from other py modules in the project
this_folder_path = os.path.dirname(__file__)
prj_root_folder_path = os.path.join(this_folder_path, '..')
sys.path.append(prj_root_folder_path)

from src import settings