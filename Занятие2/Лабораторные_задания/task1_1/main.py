def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return len(max(i for i in list_words))


if __name__ == "__main__":
    print(task())
