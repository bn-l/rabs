# rabs 

### Relative to absolute file names

Converts a string path that is **relative to the calling file** to an absolute path. 


#### Usage:

`function: real_to_abs_filename`

Args:
    path: str
    ret:  ret: Literal["string","path"] = "string"


```python

from rabs import real_to_abs_filename

real_to_abs_filename(".", ret="string") # the default

real_to_abs_filename("../siblingfolder/someotherfile.py")

# or 

real_to_abs_filename("./somefile.exe", ret="path")

# returns a pathlib.Path object (python's built in library)

```

#### Why:

Python is inconsistent with respect to relative paths. This makes it as bulletproof as possible.