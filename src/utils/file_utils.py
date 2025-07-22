# utils/file_utils.py
import os
import logging
from pathlib import Path

def setup_logger(name="pdf_pipeline", level=logging.INFO):
    """Configure and return a logger."""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

def ensure_dir(path: str):
    """Create directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def list_pdfs(pdf_dir: str):
    """Return list of all PDF files in directory."""
    return list(Path(pdf_dir).rglob("*.pdf"))

def get_file_name(path: str):
    """Extract filename from full path."""
    return Path(path).name

def load_json(path):
    import json
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data, path):
    import json
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def current_timestamp():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()
