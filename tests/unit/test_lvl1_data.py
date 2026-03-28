import pytest
from pathlib import Path

from rd_test_utils.fixtures.lvl1 import DATA_ROOT


@pytest.mark.parametrize("fname, expected", [
    ("ROUTE_NODES_DICT.gzip", True),
    ("ROUTE_PROFILE.gzip", True),
    ("ROUTE_WAYS_DICT.gzip", True),
    ("ROUTES_DICT.gzip", True),
    ("SR_ROUTES_DICT.gzip", True),
    ("SUPERROUTE_PROFILE.gzip", True),
    ("SUPERROUTES_DICT.gzip", True),
    ("SUPERROUTES_DICT.pkl", False),
    ("SUPER_X_DICT.gzip", False),

    ("MTB_ROUTE_NODES_DICT.gzip", True),
    ("MTB_ROUTE_PROFILE.gzip", True),
    ("MTB_ROUTE_WAYS_DICT.gzip", True),
    ("MTB_ROUTES_DICT.gzip", True),
    ("MTB_SR_ROUTES_DICT.gzip", True),
    ("MTB_SUPERROUTE_PROFILE.gzip", True),
    ("MTB_SUPERROUTES_DICT.gzip", True),

    ("HIKING_ROUTE_NODES_DICT.gzip", True),
    ("HIKING_ROUTE_PROFILE.gzip", True),
    ("HIKING_ROUTE_WAYS_DICT.gzip", True),
    ("HIKING_ROUTES_DICT.gzip", True),
    ("HIKING_SR_ROUTES_DICT.gzip", True),
    ("HIKING_SUPERROUTE_PROFILE.gzip", True),
    ("HIKING_SUPERROUTES_DICT.gzip", True),
])
def test_route_data_file_exists(fname, expected):
    
    if expected:
        assert Path(DATA_ROOT / fname).exists()
    else:
        assert not Path(DATA_ROOT / fname).exists()

@pytest.mark.parametrize("fname, expected", [
    ("TAGSET_DICT.gzip", True),
    ("TAGSET_DICT.pkl", True),
    ("CW_TAGSET_DICT.gzip", True),
    ("CW_TAGSET_DICT.pkl", True),
    ("HIKE_TAGSET_DICT.gzip", True),
    ("HIKE_TAGSET_DICT.pkl", True),

    ("NODES_TAGSETS_DICT.gzip", True),
    ("NODES_TAGSETS_DICT.pkl", True),

    ("REV_HIKE_TAGSET_DICT.gzip", True),
    ("REV_HIKE_TAGSET_DICT.pkl", True),

    ("TAG_COMBI_DICT.gzip", True),
    ("TAG_COMBI_DICT.pkl", True),
    ("REV_TAGSET_COMBI_DICT.gzip", True),
    ("REV_TAGSET_COMBI_DICT.pkl", True),

    ("REV_TAG_COMBI_DICT.gzip", False),
    ("REV_TAG_COMBI_DICT.pkl", False),
])
def test_tagset_data_file_exists(fname, expected):
    
    if expected:
        assert Path(DATA_ROOT / fname).exists()
    else:
        assert not Path(DATA_ROOT / fname).exists()
