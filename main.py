def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words in the document")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


if __name__ == "__main__":
    main()