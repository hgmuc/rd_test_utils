import pytest
import pandas as pd
from pathlib import Path

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
