import os
import logging
from pathlib import Path # for window path 

project_name = "cnnclassification"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files_of_paths = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "templates/index.htm",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "setup.py",
    "requirements.txt",
    "research/trails.ipynb",

]

for filepath in files_of_paths:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for file name {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.INFO(f"filepath already exists : {filepath}")