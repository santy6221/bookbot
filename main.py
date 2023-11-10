def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    total_letters = get_book_Letters(text)
    print(f"{num_words} words found in the document")
    for letter, frequency in total_letters.items():
        print(f"The letter {letter} has been found {frequency} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_Letters(text):
    all_lower = text.lower()
    letters = {
        "a":all_lower.count("a"),
        "b":all_lower.count("b"),
        "c":all_lower.count("c"),
        "d":all_lower.count("d"),
        "e":all_lower.count("e"),
        "f":all_lower.count("f"),
        "g":all_lower.count("g"),
        "h":all_lower.count("h"),
        "i":all_lower.count("i"),
        "j":all_lower.count("j"),
        "k":all_lower.count("k"),
        "l":all_lower.count("l"),
        "m":all_lower.count("m"),
        "n":all_lower.count("n"),
        "o":all_lower.count("o"),
        "p":all_lower.count("p"),
        "q":all_lower.count("q"),
        "r":all_lower.count("r"),
        "s":all_lower.count("s"),
        "t":all_lower.count("t"),
        "u":all_lower.count("u"),
        "v":all_lower.count("v"),
        "w":all_lower.count("w"),
        "x":all_lower.count("x"),
        "y":all_lower.count("y"),
        "z":all_lower.count("z"),
    }
    return dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))


main()