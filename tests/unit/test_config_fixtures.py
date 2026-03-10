import pytest
from pathlib import Path
from rd_test_utils.fixtures.config import (
    data_base_path,
    data_base_path_prod,
)


def test_data_base_path(data_base_path):
    """Verify pbf_dir returns a Path object pointing to the correct data folder."""
    print("data_base_path", data_base_path)
    assert isinstance(data_base_path, Path)
    assert data_base_path.is_absolute()
    assert data_base_path.name == "data"
    assert data_base_path.parent.name == "rd_test_utils"

def test_data_base_path_prod_str_format(data_base_path_prod):
    """Verify pbf_dir_str is a string representation of the data path."""
    print("data_base_path_prod", data_base_path_prod)
    assert isinstance(data_base_path_prod, str)
    # Check that it uses forward slashes or matches the platform's Path string
    assert data_base_path_prod.endswith("osmium")

