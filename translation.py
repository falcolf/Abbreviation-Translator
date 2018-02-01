def file_to_dictionary(filename):
    dictionary = {}
    opened_file = open(filename, "r")
    for line in opened_file:
        pair = line.split(":")
        dictionary[pair[0]] = pair[1].rstrip()

    opened_file.close()
    return dictionary


def translate_abbreviation(dictionary, abbreviation):
    last_character = abbreviation[-1]
    if last_character in ".?!,;:":
        abbreviation = abbreviation.rstrip(last_character)
    else:
        last_character = ""

    # translate abbreviation
    if abbreviation in dictionary:
        word = dictionary[abbreviation]
    else:
        word = abbreviation

    return word + last_character


def translate_message(dictionary, message):
    output_translation = ""
    for line in message.split():
        output_translation += translate_abbreviation(dictionary, line) + " "
    return output_translation
