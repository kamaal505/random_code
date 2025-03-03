import json

def extract_keys(obj, parent_key='', keys_set=None):
    """
    Recursively extracts all keys from a JSON object.

    :param obj: The JSON object (dict or list)
    :param parent_key: The prefix for nested keys (used for hierarchical keys)
    :param keys_set: A set to store unique keys
    :return: A set of unique keys
    """
    if keys_set is None:
        keys_set = set()

    if isinstance(obj, dict):
        for key, value in obj.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys_set.add(full_key)
            extract_keys(value, full_key, keys_set)
    elif isinstance(obj, list):
        for item in obj:
            extract_keys(item, parent_key, keys_set)

    return keys_set

def save_keys_to_file(json_file, output_file):
    """
    Extracts all keys from a JSON file and saves them to a text file.

    :param json_file: Path to the input JSON file
    :param output_file: Path to the output text file
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    keys = extract_keys(data)

    with open(output_file, 'w', encoding='utf-8') as file:
        for key in sorted(keys):
            file.write(key + '\n')

    print(f"Extracted {len(keys)} keys and saved to {output_file}")

# Example Usage
input_json = input("Please enter file path: ")
save_keys_to_file(input_json, "keys.txt")
