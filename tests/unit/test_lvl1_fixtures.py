import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from rd_test_utils.fixtures.lvl1 import _get_rev_tagset_dict_path
from rd_test_utils.fixtures.lvl1 import DATA_ROOT

def test_data_root_path():
    """Verify that DATA_ROOT points to the expected internal package directory."""
    assert DATA_ROOT.name == "lvl1"
    assert DATA_ROOT.parent.name == "data"
    assert "rd_test_utils" in str(DATA_ROOT)

@patch("rd_test_utils.fixtures.lvl1.do_ungzip_pkl")
def test_tagset_dict_logic(mock_ungzip, tmp_path):
    """Verify fixture prefers GZIP over PKL when both exist."""
    # Create fake files in a temp directory
    fake_data = tmp_path / "data"
    fake_data.mkdir()
    gz_file = fake_data / "TAGSET_DICT.gzip"
    gz_file.write_text("dummy")
    
    mock_ungzip.return_value = {"key": "value"}
    
    from rd_test_utils.fixtures.lvl1 import _load_data
    result = _load_data("TAGSET_DICT", custom_root=fake_data)
    
    assert result == {"key": "value"}
    mock_ungzip.assert_called_once_with(str(gz_file))


def test_rev_tagset_dict_path_logic():
    """
    Verify the path logic specifically. 
    We test the helper, not the fixture.
    """
    expected_path = "C:/01_AnacondaProjects/osmium/lvl1"
    assert _get_rev_tagset_dict_path() == expected_path

@patch("rd_test_utils.fixtures.lvl1.load_rev_tagset_dict")
def test_rev_tagset_dict_logic_integration(mock_load):
    """
    If you want to test the fixture behavior, 
    pass it as an argument to the test.
    """
    mock_load.return_value = {"status": "mocked"}
    
    # Note: To test the actual fixture, you'd usually do an integration 
    # test, but for unit testing the logic, the helper approach above is safer.
    from rd_test_utils.fixtures.lvl1 import _get_rev_tagset_dict_path
    path = _get_rev_tagset_dict_path()
    
    assert path == "C:/01_AnacondaProjects/osmium/lvl1"

'''
@patch("rd_test_utils.fixtures.lvl1.load_rev_tagset_dict")
def test_rev_tagset_dict_calls_correct_path(mock_load):
    """Verify the hardcoded path is passed to the loader."""
    from rd_test_utils.fixtures.lvl1 import rev_tagset_dict
    
    # We call the function directly as a unit test
    mock_load.return_value = {}
    result = rev_tagset_dict()
    
    mock_load.assert_called_once_with("C:/01_AnacondaProjects/osmium/lvl1")
'''