import searcher


def print_words(words_colletion):
    for word in words_colletion:
        print(word.replace("\n", ""))


words_colletion = searcher.main("src/rules.json", "words.txt")
print_words(words_colletion)
