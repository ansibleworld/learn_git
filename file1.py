import os
from pathlib import Path
import shutil

tmp_path = Path("this_is_my_dir")
tmp_path.mkdir(exist_ok=True)
(tmp_path / "file1.txt").touch()
(tmp_path / "file2.txt").touch()
(tmp_path / "new_dir").mkdir(exist_ok=True)
(tmp_path /"new_dir" / "file3.txt").touch()

shutil.rmtree(tmp_path)
