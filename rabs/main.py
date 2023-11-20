from pathlib import Path
import sys
import os
from typing import Literal


def real_to_abs_filename(relative_path: str, ret: Literal["string","path"]="string") -> str | Path:
    """
    Convert a relative path to an absolute one in a consistent way--no matter what the current working directory is. The file must exist, 
    
    Examples
    --------
    ".." or "." or "../some-folder" or even ".\\windows folder" 
    """

    # Extremely hacky but this is the best way I can find. Assumes the frame below (top down) is the python caller--which is hopefully always right. 
    # caller_filename = inspect.stack()[1].filename
    caller_filename = sys._getframe(1).f_code.co_filename

    caller_directory = os.path.dirname(os.path.abspath(caller_filename))
    pypath = Path(caller_directory) / relative_path
    
    return str(pypath.resolve()) if ret=="string" else pypath.resolve()
