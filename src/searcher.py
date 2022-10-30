import json

# OPTIMAL WORDS IN COMBINATION
## RECUO & LISTA
## SERIO & CULTA


def get_words_colletion(words_path):
    file = open(words_path, "r")

    words_collection = file.readlines()
    normalized_words = []

    for line in words_collection:
        normalized_words.append(line.replace("\n", ""))

    return normalized_words


def search_known_letters(rules, words_collection):
    if not rules:
        return words_collection

    filtered_words = words_collection
    should_remove_words = []

    for word in filtered_words:
        should_remove = 0
        for rule in rules:
            letter = rule["letter"]
            position = rule["position"]
            if word[position] != letter:
                should_remove = should_remove + 1

        if should_remove != 0:
            should_remove_words.append(word)
    
    for word in should_remove_words:
        filtered_words.remove(word)

    return filtered_words


def search_unknown_letters(unknown_letters, words_collection, flag=0):
    if not unknown_letters:
        return words_collection

    for letter in unknown_letters:
        words_collection = search_unknown_letter(letter, words_collection)

    return words_collection


def search_unknown_letter(letter, words_collection):

    filtered_words = words_collection
    should_not_remove_words = []

    for word in words_collection:
        should_not_remove = 0
        for index, character in enumerate(word):
            last_character = "#" if index == 0 else word[index - 1]
            if character == letter and character != last_character:
                should_not_remove = should_not_remove + 1

        if should_not_remove == 0:
            should_not_remove_words.append(word)

    for word in should_not_remove_words:
        filtered_words.remove(word)

    return filtered_words


def remove_letters(remove_letters, words_collection):
    if not remove_letters:
        return words_collection

    for letter in remove_letters:
        words_collection = remove_letter(letter, words_collection)

    return words_collection


def remove_letter(letter, words_collection):
    filtered_words = words_collection
    should_remove_words = []

    for word in words_collection:
        should_remove = 0
        for index, character in enumerate(word):
            if character == letter:
                should_remove = 1

        if should_remove == 1:
            should_remove_words.append(word)

    for word in should_remove_words:
        filtered_words.remove(word)

    return filtered_words


def validate_rules(all_rules):
    error_message = ""

    if len(all_rules["known_letters"]) > 5:
        error_message = (
            "THE KNOWN LETTERS RULES COLLECTION SHOULD NOT HAVE MORE THAN 5 LETTERS"
        )

    if len(all_rules["unknown_letters"]) > 5:
        error_message = (
            "THE UNKNOWN LETTERS RULES COLLECTION SHOULD NOT HAVE MORE THAN 5 LETTERS"
        )

    if len(all_rules["exclude_letters"]) > 5:
        error_message = (
            "THE EXCLUDE LETTERS RULES COLLECTION SHOULD NOT HAVE MORE THAN 5 LETTERS"
        )

    if error_message:
        raise OverflowError(error_message)


def main(rules_path, words_path):

    with open(rules_path) as json_file:
        all_rules = json.load(json_file)

    validate_rules(all_rules)

    known_letters_rules = all_rules["known_letters"]
    unknown_letters_rules = all_rules["unknown_letters"]
    exclude_letters_rules = all_rules["exclude_letters"]

    words_collection = get_words_colletion(words_path)

    words_collection = search_known_letters(known_letters_rules, words_collection)
    words_collection = search_unknown_letters(unknown_letters_rules, words_collection)
    words_collection = remove_letters(exclude_letters_rules, words_collection)

    return words_collection


def get_dummy():
    return 10
