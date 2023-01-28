import pytest
from deepClassifier.utils import read_yaml_file
from pathlib import Path
from box import ConfigBox


yaml_files = [
    "tests/data/empty.yaml",
    "tests/data/demo.yaml"]

def test_read_yaml_empty():
    with pytest.raises(ValueError):
        read_yaml_file(Path(yaml_files[0]))
        

