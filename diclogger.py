import logging
import json
import logging.config
from typing import Dict, Any

def configure_logging(verbose: bool):
    if not isinstance(verbose , bool):
        raise TypeError
    base_config : Dict[str, Any] = {
        "version" : 1,
        "disable_existing_logger": True,
        "formatters":{
            "simple":{"format" : "%(levelname)s:%(message)s"}
        },
        "handlers" :{
            "console" : {
                "class" : "logging.StreamHandler",
                "level" : "DEBUG",
                "formatter" : "simple",
            }
        },
        "root": {
            "level" : "INFO",
            "handlers": ["console"]
        }
    } 
    if verbose:
        base_config["root"]["level"] = "DEBUG"
    logging.config.dictConfig(base_config)
    return logging.getLogger()

