import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def show_data(data):
    """Iterates through JSON data and prints it."""
    for animal in data:
        if "name" in animal:
            name = animal["name"]
            print(f"Name: {name}")
        if "diet" in animal["characteristics"]:
            diet = animal["characteristics"]["diet"]
            print(f"Diet: {diet}")
        if "locations" in animal:
            location = animal["locations"][0]
        print(f"Location: {location}")
        if "type" in animal["characteristics"]:
            type_ = animal["characteristics"]["type"]
            print(f"Type: {type_}")


def main():
    animals_data = load_data('animals_data.json')
    show_data(animals_data)


if __name__ == "__main__":
    main()
