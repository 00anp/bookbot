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
    
    def get_letter_report(letter_count):
        report = ""
        for k,v in letter_count.items():
            report += f"The '{k}' character was found {v} times\n"
        return report

    def get_report(path, word_count, letter_report):
        report = f"""--- Begin report of {path} ---
{word_count} words found in the document
{letter_report}
--- End report ---"""
        return report

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)[0]
    words = count_words(text)[1]
    letters = count_letters(words)
    sorted_letters = dict(sorted(letters.items(), key=lambda x:x[1], reverse=True))
    letter_report = get_letter_report(sorted_letters)
    report = get_report(book_path, word_count, letter_report)
    print(report)


main()