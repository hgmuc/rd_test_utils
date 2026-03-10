import pytest
from pathlib import Path
from basic_helpers.file_helper import do_ungzip_pkl #, do_unpickle
from lvl2_env_api.env_config import load_rev_tagset_dict

# Helper to find the package data directory relative to this file
DATA_ROOT = Path(__file__).resolve().parent / "data" / "lvl1"


@pytest.fixture(scope="session")
def tagset_dict():
    #BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    print("DATA_ROOT - tagset_dict", str(DATA_ROOT))
    TAGSET_DICT_GZIP = DATA_ROOT / "TAGSET_DICT.gzip"
    TAGSET_DICT_PKL = DATA_ROOT / "TAGSET_DICT.pkl"
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
    #BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    REV_TC_PATH_GZIP = DATA_ROOT / "REV_TAGSET_COMBI_DICT.gzip"
    REV_TC_PATH_PKL = DATA_ROOT / "REV_TAGSET_COMBI_DICT.pkl"
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
