import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def pbf_dir():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return BASE_DIR / "data" / "raw"

@pytest.fixture(scope="session")
def pbf_dir_str():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/data/raw"

@pytest.fixture(scope="session")
def monaco_pbf():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/data/raw/monaco-latest.osm.pbf"

@pytest.fixture(scope="session")
def liechtenstein_pbf():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/data/raw/liechtenstein-latest.osm.pbf"

@pytest.fixture(scope="session")
def san_marino_bz2():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/data/raw/san-marino-overpass.osm.bz2"
