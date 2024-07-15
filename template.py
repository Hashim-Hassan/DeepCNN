import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

project_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constatnts/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml", #Data Version Control
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml", # Required if we're creating a python packages
    "tox.ini", # Used for testing a project locally
    "research/trials.ipynb" #Jupyter notebook file for trial purposes
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory: {fileDir} for file: {fileName}")
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath, 'w') as f:
            pass # Create an empty file
            logging.info(f"Creating directory: {fileDir}")
    else:
        logging.info(f"{fileName} already exists")
