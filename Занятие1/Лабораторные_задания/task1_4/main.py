def list_comprehension(words: list) -> list:
    return [words for words in list_words.capitalize()]


def list_map(words: list) -> list:
    return list(...)  # TODO


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]

    print(list_comprehension(list_words))
    print(list_map(list_words))


if __name__ == "__main__":
    task()
