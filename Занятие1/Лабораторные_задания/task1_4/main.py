def list_comprehension(words: list) -> list:
    return [words for words in list(words.capitalize())]


def list_map(words: list) -> list:
    return list(map(list_map, words))


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]
    list = list_words.lower()
    print(list_comprehension(list_words))
    print(list_map(list_words))
    print(list)

if __name__ == "__main__":
    task()
