import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : [%(message)s]')

package_name = 'deepClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/config/__init__.py", 
    f"src/{package_name}/constant/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integrate/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requiremnts.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trails.ipynb"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory : {file_dir} for {file_name}')
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w'):
            pass
            logging.info(f'Creating empty file : {file_path}')
    else:
        logging.info(f'{file_name} already exits')
    