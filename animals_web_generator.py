import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file):
    """ Reads html file and returns string """
    with open(file, "r") as fileobj:
        return fileobj.read()


def serialize_animal(animal_obj):
    """ Iterates through JSON data and returns extracted data """
    output = '            <li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'              <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '              <p class="card__text">\n'
    if "diet" in animal_obj["characteristics"]:
        output += f'                  <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj:
        output += f'                  <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if "type" in animal_obj["characteristics"]:
        output += f'                  <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '              </p>\n            </li>\n'
    return output


def write_html(html_data, output, file):
    """ Inserts extracted data from JSON file in the html string and overwrites html file"""
    new_html_data = html_data[:1738] + output + '        </ul>\n    </body>\n</html>'
    with open(file, "w") as fileobj:
        fileobj.write(new_html_data)


def main():
    """ Gets specific data from JSON file and inserts it into html file """
    animals_data = load_data('animals_data.json')
    old_html_data = read_html('animals_template.html')
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    write_html(old_html_data, output, 'animals_template.html')


if __name__ == "__main__":
    main()
