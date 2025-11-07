import json

def load_database(file_path = './database/db.json'):
    """Load the database from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
