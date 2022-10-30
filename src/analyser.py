import json


def get_words_collection(words_path):
    file = open(words_path, "r")

    words_collection = file.readlines()
    normalized_words = []

    for line in words_collection:
        normalized_words.append(line.replace("\n", ""))

    return normalized_words


def unique_letter_count():
    words_collection = get_words_collection("words.txt")
    global_letter_count = 0
    unique_letters_collection = []
    unique_letters_counters = []

    for word in words_collection:
        for letter in word:
            if letter not in unique_letters_collection:
                unique_letters_collection.append(letter)

    for unique_letter in unique_letters_collection:
        unique_letter_count = 0
        for word in words_collection:
            for letter in word:
                if letter == unique_letter:
                    unique_letter_count = unique_letter_count + 1

        unique_letters_counters.append(
            {"letter": unique_letter, "count": unique_letter_count}
        )

    return sorted(
        unique_letters_counters,
        key=lambda element: element["count"],
        reverse=True,
    )


def unique_non_vowel_counter():
    words_collection = get_words_collection("words.txt")
    non_vowels_words_collection = []
    vowels = ["A", "E", "I", "O", "U"]

    for word in words_collection:
        non_vowel_count = 0
        non_vowel_list = []
        for letter in word:
            if letter not in vowels and letter not in non_vowel_list:
                non_vowel_list.append(letter)
                non_vowel_count = non_vowel_count + 1

        vowels_word = {
            "word": word,
            "non_vowel_count": non_vowel_count,
            "non_vowel_list": non_vowel_list,
        }
        non_vowels_words_collection.append(vowels_word)

    return sorted(
        non_vowels_words_collection,
        key=lambda element: element["non_vowel_count"],
        reverse=True,
    )


def unique_vowel_counter():
    words_collection = get_words_collection("words.txt")
    vowels_words_collection = []
    vowels = ["A", "E", "I", "O", "U"]

    for word in words_collection:
        vowel_count = 0
        vowel_list = []
        for letter in word:
            if letter in vowels and letter not in vowel_list:
                vowel_list.append(letter)
                vowel_count = vowel_count + 1

        vowels_word = {
            "word": word,
            "vowel_count": vowel_count,
            "vowel_list": vowel_list,
        }
        vowels_words_collection.append(vowels_word)

    return sorted(
        vowels_words_collection,
        key=lambda element: element["vowel_count"],
        reverse=True,
    )


def get_csv(collection, file_name, headers):

    with open(f"{file_name}.csv", "w") as file:
        for header in headers:
            file.write("%s;" % (header.upper()))
        file.write("\n")

        for object in collection:
            for key in object.keys():
                file.write("%s;" % (object[key]))
            file.write("\n")


def main():
    vowel_collection = unique_vowel_counter()
    non_vowel_collection = unique_non_vowel_counter()
    unique_letters = unique_letter_count()

    get_csv(vowel_collection, "t_vowel_collection", ["word", "vowel_count", "vowel_list"])
    get_csv(non_vowel_collection, "t_non_vowel_collection", ["word", "non_vowel_count", "non_vowel_list"])
    get_csv(unique_letters, "t_unique_letters", ["letter", "count"])


main()
