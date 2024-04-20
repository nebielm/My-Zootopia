import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file):
    """ Reads html file and returns string """
    with open(file, "r") as fileobj:
        return fileobj.read()


def extract_data(data):
    """ Iterates through JSON data and returns extracted data """
    output = ''
    for animal in data:

        if "name" in animal:
            output += f"            Name: {animal["name"]}\n"
        if "diet" in animal["characteristics"]:
            output += f"            Diet: {animal["characteristics"]["diet"]}\n"
        if "locations" in animal:
            output += f"            Location: {animal["locations"][0]}\n"
        if "type" in animal["characteristics"]:
            output += f"            Type: {animal["characteristics"]["type"]}\n"
        output += "\n"
    return output


def write_html(html_data, output, file):
    """ Inserts extracted data from JSON file in the html string and overwrites html file"""
    new_data = html_data.replace("            __REPLACE_ANIMALS_INFO__\n", output)
    with open(file, "w") as fileobj:
        fileobj.write(new_data)


def main():
    """ Gets specific data from JSON file and inserts it into html file """
    animals_data = load_data('animals_data.json')
    old_html_data = read_html('animals_template.html')
    extracted_animals_data = extract_data(animals_data)
    write_html(old_html_data, extracted_animals_data, 'animals_template.html')


if __name__ == "__main__":
    main()
