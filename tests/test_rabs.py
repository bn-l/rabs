import pytest
from pathlib import Path
from rabs import real_to_abs_filename

@pytest.mark.parametrize("relative_path, expected", [
    (".", Path(__file__).parent.resolve()),
    ("./somefile.py", (Path(__file__).parent / "somefile.py").resolve()),
    ("./", Path(__file__).parent.resolve()),
    ("../parentfolder/sibling/somefile.py", (Path(__file__).parent.parent / "parentfolder/sibling/somefile.py").resolve()),
])
def test_real_to_abs_filename_path(relative_path, expected):
    assert real_to_abs_filename(relative_path, ret="path") == expected

@pytest.mark.parametrize("relative_path", [
    ".",
    "./somefile.py",
    "./",
    "../parentfolder/sibling/somefile.py"
])
def test_real_to_abs_filename_string(relative_path):
    expected = str((Path(__file__).parent / relative_path).resolve())
    assert real_to_abs_filename(relative_path, ret="string") == expected

@pytest.mark.parametrize("relative_path, ret_type", [
    (".", "string"),
    (".", "path"),
    ("./somefile.py", "string"),
    ("./somefile.py", "path")
])
def test_real_to_abs_filename_return_type(relative_path, ret_type):
    result = real_to_abs_filename(relative_path, ret=ret_type)
    assert isinstance(result, str if ret_type == "string" else Path)
