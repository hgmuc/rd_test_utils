import pytest
from pathlib import Path

from rd_test_utils.fixtures.lvl2 import DATA_ROOT

@pytest.mark.parametrize("this_path, expected", [
    (Path(DATA_ROOT / "admin-csv" / "admin8.csv"), True),
    (Path(DATA_ROOT / "admin-csv" / "admin6.csv"), False),
    (Path(DATA_ROOT / "admin-csv" / "admin7.csv"), False),
    (Path(DATA_ROOT / "admin-csv" / "admin9.csv"), False),
    (Path(DATA_ROOT / "admin-csv" / "admin10.csv"), False),

    (Path(DATA_ROOT / "admin-to-cells" / "ADMIN_ID_HIERARCHY.pkl"), True),
    (Path(DATA_ROOT / "admin-to-cells" / "ADMIN_TO_CELLS.pkl"), False),
    (Path(DATA_ROOT / "admin-to-cells" / "ADMIN_TO_CELLS.gzip"), True),
    (Path(DATA_ROOT / "admin-to-cells" / "REGION_BBOX.pkl"), True),
    (Path(DATA_ROOT / "admin-to-cells" / "REGION_BBOX_DICT.pkl"), True),
    (Path(DATA_ROOT / "admin-to-cells" / "REGION_BBOX_DICT.gzip"), False),
    
    (Path(DATA_ROOT / "admin4-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "admin4-dach" / "BN.txt"), True),
    (Path(DATA_ROOT / "admin4-dach" / "KL.txt"), True),
    (Path(DATA_ROOT / "admin4-dach" / "OP.txt"), False),

    (Path(DATA_ROOT / "admin5-dach" / "AM.txt"), False),
    (Path(DATA_ROOT / "admin5-dach" / "BN.txt"), True),

    (Path(DATA_ROOT / "admin6-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "admin6-dach" / "BN.txt"), True),

    (Path(DATA_ROOT / "admin7-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "admin7-dach" / "BN.txt"), True),
    (Path(DATA_ROOT / "admin7-dach" / "KL.txt"), True),
    (Path(DATA_ROOT / "admin7-dach" / "OP.txt"), False),

    (Path(DATA_ROOT / "admin8-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "admin8-dach" / "BN.txt"), True),

    (Path(DATA_ROOT / "admin9-dach" / "AM.txt"), False),
    (Path(DATA_ROOT / "admin9-dach" / "BN.txt"), False),

    (Path(DATA_ROOT / "admin10-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "admin10-dach" / "BN.txt"), True),

    (Path(DATA_ROOT / "code2admin-dach" / "AM.txt"), False),

    (Path(DATA_ROOT / "code2admin-dach" / "AM.pkl"), True),
    (Path(DATA_ROOT / "code2admin-dach" / "BN.pkl"), True),
    (Path(DATA_ROOT / "code2admin-dach" / "KL.pkl"), True),
    (Path(DATA_ROOT / "code2admin-dach" / "OP.pkl"), False),

])
def test_admin_data_file_exists(this_path, expected):
    
    if expected:
        assert this_path.exists()
    else:
        assert not this_path.exists()


@pytest.mark.parametrize("this_path, expected", [
    (Path(DATA_ROOT / "code2env-dach" / "CODE_TO_ENV_9N.gzip"), False),
    (Path(DATA_ROOT / "code2env-dach" / "CODE_TO_ENV_BN.gzip"), True),

    (Path(DATA_ROOT / "env-coastline-dach" / "9N.txt"), True),
    (Path(DATA_ROOT / "env-coastline-dach" / "AM.txt"), False),

    (Path(DATA_ROOT / "env-farmland-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-forest-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-highways-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-locality-nodes-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-mountain-passes-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-natural-peaks-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-nature-reserve-dach" / "AM.txt"), True),

    (Path(DATA_ROOT / "env-railways-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-region-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-residential-dach" / "AM.txt"), True),

    (Path(DATA_ROOT / "env-terrain-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-terrain-dach" / "AM_bg.txt"), True),

    (Path(DATA_ROOT / "env-tourism-nodes-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-tourism-nodes-dach" / "BN.txt"), False),
    (Path(DATA_ROOT / "env-tourism-areas-dach" / "AM.txt"), True),

    (Path(DATA_ROOT / "env-treerows-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-waterways-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "env-waypoints-dach" / "AM.txt"), False),
    (Path(DATA_ROOT / "env-waypoints-dach" / "BN.txt"), True),
])
def test_env_data_file_exists(this_path, expected):
    
    if expected:
        assert this_path.exists()
    else:
        assert not this_path.exists()

@pytest.mark.parametrize("this_path, expected", [
    (Path(DATA_ROOT / "ways-barrier-nodes-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "ways-guideposts-dach" / "AM.txt"), True),
    (Path(DATA_ROOT / "ways-guideposts-dach" / "AM_Destinations.txt"), True),

    (Path(DATA_ROOT / "ways-dach" / "A" / "AL.txt"), True),
    (Path(DATA_ROOT / "ways-dach" / "A" / "AM.txt"), True),
    (Path(DATA_ROOT / "ways-dach" / "A" / "AN.txt"), False),
])
def test_ways_data_file_exists(this_path, expected):
    
    if expected:
        assert this_path.exists()
    else:
        assert not this_path.exists()


@pytest.mark.parametrize("this_path, expected", [
    (Path(DATA_ROOT / "rd-geocode-dach" / "A" / "BASE_DATA_DF_AM.gzip"), True),
    (Path(DATA_ROOT / "rd-geocode-dach" / "A" / "GEOMETRY_AM.gzip"), False),
    (Path(DATA_ROOT / "rd-geocode-dach" / "A" / "GEOMETRY_AM.zip"), True),
    (Path(DATA_ROOT / "rd-geocode-dach" / "GEOMETRY_AM.gzip"), False),
])
def test_rd_geocode_data_file_exists(this_path, expected):
    
    if expected:
        assert this_path.exists()
    else:
        assert not this_path.exists()


@pytest.mark.parametrize("this_path, expected", [
    (Path(DATA_ROOT / "add-features-dach" / "fast_food" / "AM.txt"), True),
    (Path(DATA_ROOT / "add-features-dach" / "lighthouses" / "AM.txt"), True),
    (Path(DATA_ROOT / "add-features-dach" / "lighthouses" / "9I.txt"), True),
    (Path(DATA_ROOT / "add-features-dach" / "lighthouses" / "9J.txt"), False),
    (Path(DATA_ROOT / "add-features-dach" / "shops" / "AM.txt"), True),
    (Path(DATA_ROOT / "add-features-dach" / "vending_machines" / "AM.txt"), True),
    (Path(DATA_ROOT / "add-features-dach" / "ADD_FEAT_TAGSET_DICT.gzip"), True),
])
def test_add_features_data_file_exists(this_path, expected):
    
    if expected:
        assert this_path.exists()
    else:
        assert not this_path.exists()

