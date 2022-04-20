def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return [len(map(task, list_words))]


if __name__ == "__main__":
    print(task())
