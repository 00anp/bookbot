def main():
    def get_book_text(path):
        with open(path) as f:
            return f.read()
    
    def count_words(txt):
        word_list = txt.split()
        return len(word_list), word_list

    def count_letters(words):
        letters = {}

        for word in words:
            word = word.lower()
            for i in word:
                if i.isalpha():
                    if i in letters:
                        letters[i] += 1
                    else:
                        letters[i] = 1
        return letters


    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)[0]
    words = count_words(text)[1]
    letters = count_letters(words)
    print(letters)


    


main()