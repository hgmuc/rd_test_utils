import pytest
from pathlib import Path

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"

@pytest.fixture(scope="session")
def data_base_path():
    return DATA_ROOT

@pytest.fixture(scope="session")
def data_base_path_prod():
    return f"C:/01_AnacondaProjects/osmium"
