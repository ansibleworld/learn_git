import logging
import os
from logging.handlers import RotatingFileHandler

log_file = "rotating.txt"

# Delete old log files
for file_name in os.listdir("."):
    if file_name.startswith("rotating.txt"):
        os.remove(file_name)

# Create logger
loggerss = logging.getLogger("my_app")
loggerss.setLevel(logging.INFO)

# Prevent duplicate handlers if rerun
loggerss.handlers.clear()

# Rotating file handler
rotating_fh = RotatingFileHandler(
    log_file,
    maxBytes=1024,   # 1 KB
    backupCount=3
)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

rotating_fh.setFormatter(formatter)

# Add handler
loggerss.addHandler(rotating_fh)

# Generate logs
for i in range(10000):
    loggerss.info(f"Log message {i}")

print("Logging completed.")