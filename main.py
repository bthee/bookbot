def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(f"{num_words} words in the document")
    print(num_char)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    chars = {}
    for char in text:
        if char in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars


if __name__ == "__main__":
    main()