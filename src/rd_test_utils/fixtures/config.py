import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def data_base_path():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/data"

@pytest.fixture(scope="session")
def data_base_path_prod():
    return f"C:/01_AnacondaProjects/osmium"
