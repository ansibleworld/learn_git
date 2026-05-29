from pathlib import Path
import shutil

def create_backup(source_dir: str | Path, dest_dir: str | Path) -> None:
    if not isinstance(source_dir, (str, Path)):
        raise TypeError("source_dir must be str or Path")

    if not isinstance(dest_dir, (str, Path)):
        raise TypeError("dest_dir must be str or Path")

    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    if not source_path.exists():
        raise FileNotFoundError(f"Source does not exist: {source_path}")

    if dest_path.exists():
        shutil.rmtree(dest_path)

    shutil.copytree(source_path, dest_path)