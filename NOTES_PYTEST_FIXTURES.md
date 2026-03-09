# Question #1:
Show me how to set up fixtures for test data. Below are some examples of different formats I use internally and which I want to include in my testing strategy. Examples 1 - 3 are UTF-8 text files. There are either custom reader functions (which load from file) or the TSV file is read with the Pandas read_csv() function. It would be interesting to see, if those data snippets could become a fixture. Example files 4 - 6 are OSM data files.

Examples 1 - 6
...

And on a separate note: In your previous answer you "pass_filenames: false" in the modified pre-commit configuration, which triggered a follow-up question. Is it possible to pass a file name into a unit test? - Let's say the unit loads "monaco-latest.osm.pbf" from tests/data. - But maybe I want to run the same test "monaco-latest.osm.pbf" from prod data storage (which is potentially newer) or run "andorra-latest.osm.pbf", for which no fixture exists. So, is it possible to pass a file name to either one specific unit test or to a test_xyz.py file, where some of the unit tests pick up a custom parameter "fname" and run the test with a different file than in the usual CI?


# Answer #1
from https://chatgpt.com/c/69aeab7e-f690-832b-95ed-d6913e9e7209


You’re working with exactly the type of project where **pytest fixtures become extremely powerful**: data pipelines, geospatial processing, and file-based APIs. The goal is to make tests:

* **clean**
* **reusable**
* **fast**
* **configurable**

Below is a **professional pattern used in many data-processing libraries**.

---

## 1. Recommended Test Layout

Extend your structure slightly:

```
tests/
│
├─ conftest.py        ## shared fixtures
│
├─ data/
│   ├─ nodes_small.txt
│   ├─ ways_small.txt
│   ├─ admin_sample.tsv
│   ├─ monaco.osm.pbf
│   └─ liechtenstein.osm.pbf
│
├─ unit/
│   └─ test_geometry_decoder.py
│
└─ integration/
    └─ test_osm_loader.py
```

The **magic file is `conftest.py`**.

Pytest automatically loads fixtures from it.

---

## 2. Base Fixture: Test Data Directory

First create a reusable **data path fixture**.

#### `tests/conftest.py`

```python
from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def data_dir():
    """Return path to test data directory."""
    return Path(__file__).parent / "data"
```

Now every test can do:

```python
def test_something(data_dir):
    f = data_dir / "file.txt"
```

---

## 3. Fixture for Example #1 (custom separator file)

You can return either:

* file path
* parsed dataframe
* parsed Python objects

I usually create **both options**.

#### Path fixture

```python
@pytest.fixture
def node_file(data_dir):
    return data_dir / "nodes_small.txt"
```

---

#### Parsed dataframe fixture

```python
import pandas as pd

@pytest.fixture
def nodes_df(node_file):
    return pd.read_csv(
        node_file,
        sep="\\|#\\|",
        header=None,
        names=["node_id", "tagset_id", "lat", "lon"],
        engine="python",
    )
```

Test becomes very clean:

```python
def test_node_loading(nodes_df):
    assert len(nodes_df) > 0
    assert "lat" in nodes_df.columns
```

---

## 4. Fixture for Example #2 (geometry encoded lines)

Example fixture returning **raw rows**:

```python
@pytest.fixture
def way_file(data_dir):
    return data_dir / "ways_small.txt"
```

Or parsed:

```python
@pytest.fixture
def ways_df(way_file):
    import pandas as pd

    return pd.read_csv(
        way_file,
        sep="\\|#\\|",
        header=None,
        names=["way_id", "railtype", "ref", "flag1", "flag2", "geometry"],
        engine="python",
    )
```

Test:

```python
def test_geometry_column_exists(ways_df):
    assert "geometry" in ways_df.columns
```

---

## 5. Fixture for Example #3 (TSV with header)

Very simple.

```python
@pytest.fixture
def admin_df(data_dir):
    import pandas as pd

    return pd.read_csv(
        data_dir / "admin_sample.tsv",
        sep="\t",
    )
```

Test:

```python
def test_admin_levels(admin_df):
    assert admin_df["Level"].max() <= 8
```

---

## 6. Fixtures for OSM PBF / BZ2 files

For large files it's better to return **paths**, not loaded data.

#### PBF fixture

```python
@pytest.fixture
def osm_monaco_pbf(data_dir):
    return data_dir / "monaco-latest.osm.pbf"
```

#### BZ2 fixture

```python
@pytest.fixture
def osm_sanmarino_bz2(data_dir):
    return data_dir / "san-marino-overpass.osm.bz2"
```

Usage:

```python
def test_osm_loader(osm_monaco_pbf):
    data = load_osm_file(osm_monaco_pbf)
    assert len(data.nodes) > 0
```

---

## 7. Fixture for gzipped pickle dictionaries

Very common pattern.

```python
@pytest.fixture
def sample_pickle(data_dir):
    return data_dir / "example_dict.pkl.gz"
```

Test:

```python
def test_pickle_loader(sample_pickle):
    from basic_helpers import do_ungzip_pkl

    data = do_ungzip_pkl(sample_pickle)

    assert isinstance(data, dict)
```

---

## 8. Creating test data dynamically (extremely useful)

Sometimes you don't want files in repo.

Example:

```python
@pytest.fixture
def tmp_node_file(tmp_path):

    content = """1|#|10|#|46.1|#|11.0
2|#|10|#|46.2|#|11.1
"""

    f = tmp_path / "nodes.txt"
    f.write_text(content)

    return f
```

Test:

```python
def test_reader(tmp_node_file):
    df = my_reader(tmp_node_file)
    assert len(df) == 2
```

This is **excellent for unit tests**.

---

## 9. Parameterizing tests with different files

Very powerful feature.

Example:

```python
import pytest


@pytest.mark.parametrize(
    "fname",
    [
        "monaco-latest.osm.pbf",
        "liechtenstein-latest.osm.pbf",
    ],
)
def test_osm_loader(data_dir, fname):

    path = data_dir / fname

    data = load_osm_file(path)

    assert len(data.nodes) > 0
```

---

## 10. Passing custom file paths via CLI (your question)

Yes — pytest supports **custom command-line parameters**.

Example:

```
pytest --osmfile=/data/andorra-latest.osm.pbf
```

---

#### Add CLI option

`tests/conftest.py`

```python
def pytest_addoption(parser):
    parser.addoption(
        "--osmfile",
        action="store",
        default=None,
        help="Custom OSM file for integration tests",
    )
```

---

#### Fixture reading that option

```python
@pytest.fixture
def osm_file(request, data_dir):

    cli_value = request.config.getoption("--osmfile")

    if cli_value:
        return Path(cli_value)

    return data_dir / "monaco-latest.osm.pbf"
```

---

#### Test using it

```python
def test_osm_loader(osm_file):

    data = load_osm_file(osm_file)

    assert len(data.nodes) > 0
```

---

#### Example usage

Default CI run:

```
pytest
```

Uses:

```
tests/data/monaco-latest.osm.pbf
```

---

Local test with production file:

```
pytest --osmfile=/mnt/osm/andorra-latest.osm.pbf
```

Same test, different file.

---

## 11. Even better: dataset parametrization

Example:

```python
@pytest.fixture(params=[
    "monaco-latest.osm.pbf",
    "liechtenstein-latest.osm.pbf",
])
def osm_dataset(request, data_dir):

    return data_dir / request.param
```

Test runs **twice automatically**.

```
def test_loader(osm_dataset):
    data = load_osm_file(osm_dataset)
```

---

## 12. About `pass_filenames: false` (your question)

Pre-commit normally runs:

```
pytest file1.py file2.py
```

This breaks pytest collection sometimes.

Setting:

```
pass_filenames: false
```

means:

```
pytest
```

runs the **whole test suite** instead.

This is usually desired.

---

## 13. My recommended setup for your project

`conftest.py`

Fixtures:

```
data_dir
nodes_df
ways_df
admin_df
osm_monaco_pbf
osm_liechtenstein_pbf
sample_pickle
osm_file (CLI override)
```

Plus CLI option:

```
--osmfile
```

---

## 14. Resulting workflow

Run default tests:

```
pytest
```

Run integration with real dataset:

```
pytest --osmfile=/data/osm/andorra.osm.pbf
```

Run only integration tests:

```
pytest -m integration
```

---

