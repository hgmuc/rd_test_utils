import pytest
import pandas as pd
from pathlib import Path


import pytest
import pandas as pd
from pathlib import Path

# Helper to find the package data directory relative to this file
DATA_ROOT = Path(__file__).resolve().parent / "data" / "lvl2"

@pytest.fixture(scope="session")
def lvl2_base_dir() -> Path:
    """Returns the Path object for the lvl2 data directory."""
    return DATA_ROOT

@pytest.fixture(scope="session")
def lvl2_base_dir_str() -> str:
    """Returns the absolute string path for the lvl2 data directory."""
    return str(DATA_ROOT)

@pytest.fixture(scope="session")
def admin8_csv() -> str:
    """Returns the string path to the admin8 CSV file."""
    return str(DATA_ROOT / "admin-csv" / "admin8.csv")

@pytest.fixture(scope="session")
def admin8_df(admin8_csv: str) -> pd.DataFrame:
    """Loads the admin8 CSV into a pandas DataFrame."""
    # Reusing the admin8_csv fixture for consistency
    return pd.read_csv(admin8_csv, sep="\t", index_col=0)

@pytest.fixture(scope="session")
def add_features_shop() -> str:
    """Returns the string path to the AM shop feature file."""
    return str(DATA_ROOT / "add-features-dach" / "shop" / "AM.txt")

'''
@pytest.fixture(scope="session")
def lvl2_base_dir():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return BASE_DIR / ".." / "data" / "lvl2"

@pytest.fixture(scope="session")
def lvl2_base_dir_str():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/../data/lvl2"

@pytest.fixture(scope="session")
def admin8_csv():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/../data/lvl2/admin-csv/admin8.csv"

@pytest.fixture(scope="session")
def admin8_df():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return pd.read_csv(f"{BASE_DIR}/../data/lvl2/admin-csv/admin8.csv", sep="\t", index_col=0)

@pytest.fixture(scope="session")
def add_features_shop():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    return f"{BASE_DIR}/../data/lvl2/add-features-dach/shop/AM.txt"
'''