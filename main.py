from stats import get_num_words, characters_count

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents = f.read()

    return file_contents

def main():
    import sys 

    if len(sys.argv) < 2:
        print("""
Please provide book path as an argument
              
Usage : python3 main.py path_to_book
              """)
        sys.exit(1)

    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    count_words = get_num_words(contents)
    chars_count = sorted(characters_count(contents).items(), 
                         key=lambda x: x[1], 
                         reverse=True)
    chars_count_report = ""
    for chars in chars_count:
        if chars[0].isalpha():
            chars_count_report += f"{chars[0]}: {chars[1]}\n"
    
    r = report(book_path, count_words, chars_count_report.rstrip())
    print(r)



def report(book_path: str, word_count: int, character_count: dict[str, int]) -> str:
    return f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{character_count}
============= END ===============
    """

if __name__ == "__main__":
    main()
