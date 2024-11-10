import string

book: str = "books/frankenstein.txt" 

def main():
    with open(book) as file:
        report(file.read())

def word_count(book_content: str) -> int:
    return len(book_content.split())

def count_characters(book_content: str) -> dict:
    characters_set = dict()
    for w in book_content.lower():
        if w in characters_set:
            characters_set[w] = characters_set[w] + 1
        else:
            if w in string.ascii_lowercase:
                characters_set[w] = 1        
    return characters_set

def report(content: str) -> None:
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(content)} words found in the document") 
    content_dict = count_characters(content)
    for w in content_dict:
        print(f"The '{w}' character was found {content_dict[w]} times")
    print("--- End report ---")
if __name__ == "__main__":
    main()
