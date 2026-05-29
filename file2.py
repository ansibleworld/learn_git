import os
import shutil
from pathlib import Path

files = Path("dir1/dir5/dir3")
files.mkdir(parents=True , exist_ok=True)
print(files.exists())