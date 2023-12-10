# The main function serves as the entry point for the program.
def main()-> int:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_lower = text.lower()
    num_words = get_num_words(text_lower)
    num_char = get_num_char(text_lower)
    sorted_char = sort_char(num_char)
    print(f"{num_words} words in the document")
    print()
    for i in sorted_char:
        print(f"The '{i[1]}' character was found {i[0]} times")

# Function to read the text content of a book from a given file path.
def get_book_text(book_path: str)-> str:
    with open(book_path) as f:
        return f.read()

# Function to count the number of words in a given text.
def get_num_words(text: str)-> int:
    words = text.split()
    return len(words)

# Function to count the occurrences of each character in a given text.
def get_num_char(text: str)-> dict:
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

# 
def sort_char(sorted: dict)-> list:
    cleaned_list = []
    key = list(sorted.keys())
    value = list(sorted.values())
    for key, value in sorted.items():
        if key.isalpha():
            cleaned_list.append((value, key))
    cleaned_list.sort(reverse=True)
    return cleaned_list


# Check if the script is being run as the main program.
if __name__ == "__main__":
    main()