def read_book(title_path):
    """
    Read a book and return it as s string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

#text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
#ind = text.find("What's in a name?")
#sample_text = text[ind : ind + 1000]
    
import os

book_dir = "./Books"
for language in os.listdir(book_dir)[1:]:
    print(language)
    for author in os.listdir(book_dir + "/" + language):
        print(author)
#        for title in os.listdir(book_dir + "/" + language + "/" + author)[1:]:
#            print(title)