import json
import os
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *

# Path to the file where the store will be saved
STORE_FILE_PATH = 'store.json'

def your_custom_storage_is_empty():
    """Check if the custom storage is empty."""
    return not os.path.exists(STORE_FILE_PATH)

def load_from_your_custom_storage():
    """Load the store from the custom storage."""
    with open(STORE_FILE_PATH, 'r') as f:
        return json.load(f)

def persist_to_your_custom_storage(store):
    """Persist the store to the custom storage."""
    with open(STORE_FILE_PATH, 'w') as f:
        json.dump(store, f)

