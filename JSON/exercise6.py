import json


def create_file():
    with open('../file.json') as f:
        animals_data = json.load(f)

    for animal in animals_data['animals']:
        del animal['cat']

    with open('../new_file.json', 'w') as f:
        json.dump(animals_data, f, indent=2)


create_file()
