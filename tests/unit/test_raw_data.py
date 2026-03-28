import pytest
from pathlib import Path

from rd_test_utils.fixtures.osmium_raw import DATA_ROOT

@pytest.mark.parametrize("fname, expected", [
    ("liechtenstein-latest.osm.pbf", True),
    ("monaco-latest.osm.pbf", True),
    ("andorra-latest.osm.pbf", False),
    ("san-marino-overpass.osm.bz2", True),
    ("san-marino-latest.osm.pbf", False),
])
def test_tagset_data_file_exists(fname, expected):
    
    if expected:
        assert Path(DATA_ROOT / fname).exists()
    else:
        assert not Path(DATA_ROOT / fname).exists()
