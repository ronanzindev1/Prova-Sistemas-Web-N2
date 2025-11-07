import json

def load_database(file_path = './database/db.json'):
    """Load the database from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_database(data, file_path = './database/db.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)