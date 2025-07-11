# logs/logger.py

import logging
import os
from config.settings import LOG_DIR

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

def get_logger(name="TrapscanLogger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid duplicate handlers
    if not logger.handlers:
        # File handler
        fh = logging.FileHandler(LOG_FILE_PATH)
        fh.setLevel(logging.DEBUG)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Attach handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
