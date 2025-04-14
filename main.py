import sys

from stats import letter_count, sort_dict, word_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    book = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_freq = word_count(book)
    print(f"Found {word_freq} total words")
    print("--------- Character Count -------")
    letter_freq = letter_count(book)
    letter_freq = sort_dict(letter_freq)
    for character in letter_freq:
        if character["character"].isalpha():
            print(f"{character['character']}: {character['count']}")

    print("============= END ===============")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


main()
