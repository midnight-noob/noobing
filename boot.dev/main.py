book_path = "../github.com/midnight-noob/noobing/books/frankenstein.txt"

def main():
    text = report(book_path)
    print(text)
    for i in text:
        print(f"{i[1]} : {i[0]}")

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def num_words(book):
    text = get_book_text(book)
    words = text.split()
    return len(words)

def count_letters(string):
    letters = {}
    text = get_book_text(string)
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in "abcdefghijlmnopqrstuvxzwky":
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
    return letters

def report(lis):
    dic = count_letters(lis)
    repo = [(v, k) for k, v in dic.items()]
    repo.sort(reverse=True)
    return repo



main()