from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()

    return file_contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    count_words = get_num_words(contents)
    print(f"{count_words} words found in the document")

if __name__ == "__main__":
    main()
