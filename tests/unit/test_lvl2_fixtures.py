import pytest
import pandas as pd
from pathlib import Path
# Note: We import the fixtures directly for testing, 
# but in a real suite, pytest would find them via entry points or conftest.
from rd_test_utils.fixtures.lvl2 import (
    lvl2_base_dir,
    lvl2_base_dir_str,
    admin8_csv,
    admin8_df,
    add_features_shop
)

def test_fixtures_path_resolution(lvl2_base_dir, lvl2_base_dir_str):
    """Verify paths are absolute and point to the internal data directory."""
    assert lvl2_base_dir.is_absolute()
    print("lvl2_base_dir", str(lvl2_base_dir))
    # C:\03_PythonLibs\rd_test_utils\src\rd_test_utils\fixtures\data\lvl2
    assert "rd_test_utils\\data\\lvl2" in str(lvl2_base_dir)
    assert str(lvl2_base_dir) == lvl2_base_dir_str

def test_admin8_file_structure(admin8_csv):
    """Verify the admin8 CSV path is correct and file exists."""
    path = Path(admin8_csv)
    print("admin8_csv", str(path))
    assert path.exists()
    assert path.name == "admin8.csv"

def test_admin8_dataframe_content(admin8_df):
    """Verify the DataFrame fixture correctly parses the tab-separated file."""
    assert isinstance(admin8_df, pd.DataFrame)
    assert not admin8_df.empty
    # Verify index_col=0 worked (assuming 'id' is the first column)
    assert admin8_df.index.name is not None 

def test_shop_feature_path(add_features_shop):
    """Verify the AM.txt path resolution."""
    print("add_features_shop", add_features_shop)
    path = Path(add_features_shop)
    print("add_features_shop", add_features_shop)
    assert path.exists()
    assert path.suffix == ".txt"