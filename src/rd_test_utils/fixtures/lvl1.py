import pytest
from pathlib import Path
from basic_helpers.file_helper import do_ungzip_pkl #, do_unpickle

# Helper to find the package data directory relative to this file
DATA_ROOT = Path(__file__).resolve().parent.parent / "data" / "lvl1"


def _load_data(file_base_name: str, custom_root: Path = DATA_ROOT):
    """Helper to handle the GZIP vs PKL fallback logic."""
    gzip_path = custom_root / f"{file_base_name}.gzip"
    pkl_path = custom_root / f"{file_base_name}.pkl"
    
    try:
        if gzip_path.exists():
            return do_ungzip_pkl(str(gzip_path))
        return do_ungzip_pkl(str(pkl_path))
    except Exception as e:
        print(f"Could not load {file_base_name} from {custom_root}")
        raise e

def _get_rev_tagset_dict_path():
    return "C:/01_AnacondaProjects/osmium/lvl1"

@pytest.fixture(scope="session")
def tagset_dict():
    print("INSIDE tagset_dict()")
    return _load_data("TAGSET_DICT")

@pytest.fixture(scope="session")
def rev_tagset_dict(tagset_dict):
    #ways_base_path = f"C:/01_AnacondaProjects/osmium/lvl1"
    print("INSIDE rev_tagset_dict()", type(tagset_dict))
    return {v: k for k, v in tagset_dict.items()}

@pytest.fixture(scope="session")
def nodes_tagset_dict():
    print("INSIDE nodes_tagset_dict()")
    return _load_data("NODES_TAGSETS_DICT")

@pytest.fixture(scope="session")
def rev_nodes_tagset_dict(nodes_tagset_dict):
    #ways_base_path = f"C:/01_AnacondaProjects/osmium/lvl1"
    print("INSIDE rev_nodes_tagset_dict()", type(nodes_tagset_dict))
    return {v: k for k, v in nodes_tagset_dict.items()}

@pytest.fixture(scope="session")
def rev_tc_combi_dict():
    return _load_data("REV_TAGSET_COMBI_DICT")

@pytest.fixture(scope="session")
def rev_tc_combi_dict_prod():
    prod_root = Path("C:/01_AnacondaProjects/osmium/lvl1")
    return _load_data("REV_TAGSET_COMBI_DICT", custom_root=prod_root)



'''
@pytest.fixture(scope="session")
def tagset_dict():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    print("BASE_DIR - tagset_dict", str(BASE_DIR))
    TAGSET_DICT_GZIP = BASE_DIR / ".." / "data" / "lvl1" / "TAGSET_DICT.gzip"
    TAGSET_DICT_PKL = BASE_DIR / "lvl1" / "TAGSET_DICT.pkl"
    try:
        if TAGSET_DICT_GZIP.exists():
            return do_ungzip_pkl(str(TAGSET_DICT_GZIP))
        else:
            return do_ungzip_pkl(str(TAGSET_DICT_PKL))
    except Exception as e:
        print("Could not load TAGSET_DICT_GZIP from", str(TAGSET_DICT_GZIP))
        raise

@pytest.fixture(scope="session")
def rev_tagset_dict():
    ways_base_path = f"C:/01_AnacondaProjects/osmium/lvl1"
    return load_rev_tagset_dict(ways_base_path)


@pytest.fixture(scope="session")
def rev_tc_combi_dict():
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    REV_TC_PATH_GZIP = BASE_DIR / "lvl1" / "REV_TAGSET_COMBI_DICT.gzip"
    REV_TC_PATH_PKL = BASE_DIR / "lvl1" / "REV_TAGSET_COMBI_DICT.pkl"
    try:
        if REV_TC_PATH_GZIP.exists():
            return do_ungzip_pkl(str(REV_TC_PATH_GZIP))
        else:
            return do_ungzip_pkl(str(REV_TC_PATH_PKL))
    except Exception as e:
        print("Could not load REV_TAGSET_COMBI_DICT from", str(REV_TC_PATH_GZIP))
        raise


@pytest.fixture(scope="session")
def rev_tc_combi_dict_prod():
    BASE_DIR = Path("C:/01_AnacondaProjects/osmium")
    REV_TC_PATH_GZIP = BASE_DIR / "lvl1" / "REV_TAGSET_COMBI_DICT.gzip"
    REV_TC_PATH_PKL = BASE_DIR / "lvl1" / "REV_TAGSET_COMBI_DICT.pkl"
    try:
        if REV_TC_PATH_GZIP.exists():
            return do_ungzip_pkl(str(REV_TC_PATH_GZIP))
        else:
            return do_ungzip_pkl(str(REV_TC_PATH_PKL))
    except Exception as e:
        print("Could not load REV_TAGSET_COMBI_DICT from", str(REV_TC_PATH_GZIP))
        raise
'''
