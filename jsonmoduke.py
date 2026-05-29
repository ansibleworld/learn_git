import json
from pathlib import Path

def update_image_tag(config_path: str | Path, service_name: str, new_tag: str) -> None:
    """
    Reads a JSON config file, updates a service's image tag, and writes it back.
    """
    config_path = Path(config_path)
    if not isinstance(config_path,str):
       raise TypeError
    if not config_path.is_file:
        raise FileNotFoundError
    if service_name.strip() == "":
       raise ValueError
    if new_tag.strip() == "" :
        raise ValueError
    
    with config_path.open("r") as file:
       config_data = json.load(file)
    if service_name not in config_data :
        raise KeyError

    config_data[service_name]["image_tag"] = new_tag

    with config_path.open("W") as file:
       json.dump(config_data , file , indent=4)

    return config_path    