import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file):
    """ Reads html file and returns string """
    with open(file, "r") as fileobj:
        return fileobj.read()


def get_skin_type(animal_data):
    """ get list of skin types in  Database """
    skin_type_list = []
    for animal in animal_data:
        if "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"] not in skin_type_list:
                skin_type_list.append(animal["characteristics"]
                                      ["skin_type"].capitalize())
    skin_type_list.append("Missing skin type")
    return skin_type_list


def get_user_choice(skin_type_list):
    """ Gets user_choice of skin type """
    while True:
        user_choice = input("Enter skin type: ")
        if user_choice.capitalize() in skin_type_list:
            break
        print("You've entered a wrong choice. Try again.")
        continue
    return user_choice


def serialize_animal(animal_obj):
    """ Iterates through JSON data and returns extracted data """
    output = '            <li class="cards__item">\n'
    if "name" in animal_obj:
        output += (f'                <div class="card__title">'
                   f'{animal_obj["name"]}</div>\n')
    output += ('                <div class="card__text">\n'
               '                    <ul>\n')
    if "diet" in animal_obj["characteristics"]:
        output += (f'                        '
                   f'<li><strong>Diet:</strong> '
                   f'{animal_obj["characteristics"]["diet"]}</li>\n')
    if "locations" in animal_obj:
        output += (f'                        '
                   f'<li><strong>Location:</strong> '
                   f'{animal_obj["locations"][0]}</li>\n')
    if "type" in animal_obj["characteristics"]:
        output += (f'                        '
                   f'<li><strong>Type:</strong> '
                   f'{animal_obj["characteristics"]["type"]}</li>\n')
    output += ('                    </ul>\n                </div>\n'
               '            </li>')
    return output


def writing_new_string(animals_data, user_choice):
    """ Writing the string according to user-choice """
    output = ''
    for animal_obj in animals_data:
        if user_choice.capitalize() == "Missing skin type":
            if "skin_type" not in animal_obj["characteristics"]:
                output += serialize_animal(animal_obj)
        elif "skin_type" in animal_obj["characteristics"]:
            if (user_choice.capitalize() ==
                    animal_obj["characteristics"]["skin_type"]):
                output += serialize_animal(animal_obj)
    return output


def write_html(html_data, output, file):
    """ Inserts extracted data from JSON file
    into the html string and overwrites html file"""
    new_html_data = html_data.replace("            __REPLACE_ANIMALS_INFO__", output)
    with open(file, "w") as fileobj:
        fileobj.write(new_html_data)


def main():
    """ Gets specific data from JSON file and inserts it into html file """
    animals_data = load_data('animals_data.json')
    old_html_data = read_html('animals_template.html')
    skin_types = get_skin_type(animals_data)
    print("Available skin types:")
    for skin_type in skin_types:
        print(skin_type)
    user_choice = get_user_choice(skin_types)
    output = writing_new_string(animals_data, user_choice)
    write_html(old_html_data, output, 'new_file.html')


if __name__ == "__main__":
    main()
