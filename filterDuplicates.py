def removeDuplicatesFromListOfDictionaries(data):
    unique_data = list({frozenset(item.items()): item for item in data}.values())
    return unique_data


data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Alice"},
    {"id": 1, "name": "Alice"},  # Duplicate of id 1
    {"id": 4, "name": "Charlie"},
    {"id": 5, "name": "Bob"},
    {"id": 2, "name": "Bob"},  # Duplicate of id 2
    {"id": 6, "name": "Eve"},
    {"id": 7, "name": "Alice"},
    {"id": 3, "name": "Alice"},  # Duplicate of id 3
]
print(f'Original Length: {len(data)}')

res = removeDuplicatesFromListOfDictionaries(data)
print(res)
print(f'Length after Duplicates Removed: {len(res)}')