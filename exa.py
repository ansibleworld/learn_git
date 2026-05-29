import logging
from logging.handlers import RotatingFileHandler

def configure_rotating_logger(logger_name , log_filepath, max_size_bytes, backup_count):
    if not isinstance(logger_name, str) or not isinstance(log_filepath, str):
        raise TypeError
    if logger_name.strip() == "" or log_filepath.strip() == "":
        raise ValueError
    if not isinstance(max_size_bytes, int) or not isinstance(backup_count,int):
        raise TypeError
    if max_size_bytes <= 0 :
        raise ValueError
    if backup_count < 0:
        raise ValueError
    loggers = logging.getLogger(logger_name)
    loggers.setLevel(logging.DEBUG)
    loggers.handlers.clear()
    rotating_fh = RotatingFileHandler(filename=log_filepath, maxBytes=max_size_bytes , backupCount=backup_count)
    formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
    rotating_fh.setFormatter(formatter)
    loggers.addHandler(rotating_fh)

    return loggers
