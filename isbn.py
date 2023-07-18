import pyperclip
import sys

isbn = list(sys.argv[1]) # e.g. "9781784984892"

hyphen_indexes = [3, 5, 11, 15]

def add_hyphens_to(isbn: list[str]) -> str:
    if not len(isbn) == 13:
        print("ISBN must have 13 digits")
        return
    elif not all([i.isdigit() for i in isbn]):
        print("ISBN must only contain digits")
        return
    else:
        for i in hyphen_indexes:
            for j in range(len(isbn)):
                if i == j:
                    isbn.insert(i, "-")
                    break
    return ''.join([char for char in isbn])

def main():
    new_isbn = add_hyphens_to(isbn)    
    pyperclip.copy(new_isbn)
    print(f"{new_isbn} copied to clipboard.")

if __name__ == "__main__":
    main()

# Output: 978-1-78498-489-2