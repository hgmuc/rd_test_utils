import pytest
from pathlib import Path

DATA_ROOT = Path(__file__).resolve().parent.parent / "data" / "raw"

@pytest.fixture(scope="session")
def pbf_dir():
    return DATA_ROOT

@pytest.fixture(scope="session")
def pbf_dir_str():
    return str(DATA_ROOT)

@pytest.fixture(scope="session")
def monaco_pbf():
    return f"{DATA_ROOT}/monaco-latest.osm.pbf"

@pytest.fixture(scope="session")
def liechtenstein_pbf():
    return f"{DATA_ROOT}/liechtenstein-latest.osm.pbf"

@pytest.fixture(scope="session")
def san_marino_bz2():
    return f"{DATA_ROOT}/san-marino-overpass.osm.bz2"
