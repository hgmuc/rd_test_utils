import pytest
from pathlib import Path
from rd_test_utils.fixtures.osmium_raw import (
    pbf_dir,
    pbf_dir_str,
    monaco_pbf,
    liechtenstein_pbf,
    san_marino_bz2
)

def test_pbf_dir_type_and_path(pbf_dir):
    """Verify pbf_dir returns a Path object pointing to the correct data folder."""
    assert isinstance(pbf_dir, Path)
    assert pbf_dir.is_absolute()
    assert pbf_dir.name == "raw"
    assert pbf_dir.parent.name == "data"

def test_pbf_dir_str_format(pbf_dir_str):
    """Verify pbf_dir_str is a string representation of the data path."""
    assert isinstance(pbf_dir_str, str)
    # Check that it uses forward slashes or matches the platform's Path string
    assert pbf_dir_str.endswith("raw")

def test_monaco_pbf_path(monaco_pbf):
    """Verify the monaco pbf path string construction."""
    assert isinstance(monaco_pbf, str)
    assert monaco_pbf.endswith("monaco-latest.osm.pbf")
    # Verify it's an absolute-looking path (starts with / or C:)
    assert Path(monaco_pbf).is_absolute()

def test_liechtenstein_pbf_path(liechtenstein_pbf):
    """Verify the liechtenstein pbf path string construction."""
    assert "liechtenstein-latest.osm.pbf" in liechtenstein_pbf
    assert isinstance(liechtenstein_pbf, str)

def test_san_marino_bz2_path(san_marino_bz2):
    """Verify the san-marino bz2 path string construction."""
    assert san_marino_bz2.endswith("san-marino-overpass.osm.bz2")
    assert isinstance(san_marino_bz2, str)