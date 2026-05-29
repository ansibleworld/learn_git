from pathlib import Path 
from typing import Union
from datetime import datetime

def archive_log_files(log_directory: Union[str, Path], archive_date: str) -> list[Path]:
    log_directory = Path(log_directory)
    if not log_directory.exists() or not log_directory.is_dir():
        raise ValueError
    if not isinstance(archive_date , str):
        raise TypeError
    try:
        datetime.strptime(archive_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date")
    rename_file=[]
    for item in log_directory.iterdir():
        if item.suffix == ".log":
            new_name = f"{item.stem} - {archive_date}.log"
            new_path = item.with_name(new_name)

            item.rename(new_path)
            rename_file.append(new_path)
    return rename_file






    
