text = " This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    """
    count the number of times each word occurs in text (str). Return dictionary 
    where keys are unique words and values are word counts. Skip punctuation.
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts= {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts


from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = Counter(text.split(" "))
    return word_counts

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
    

def word_stats(word_counts):
    """Retrun number of unique words and word frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

#text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
#word_counts = count_words(text)
#(num_unique, counts) = word_stats(word_counts)
#print(num_unique, sum(counts))
#
#text = read_book("./Books/German/shakespeare/Romeo und Julia.txt")
#word_counts = count_words(text)
#(num_unique, counts) = word_stats(word_counts)
#print(num_unique, sum(counts))
    
import os
import pandas as pd

title_num = 1
book_dir = "./Books"
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
for language in os.listdir(book_dir)[1:]:
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

#stats[stats.language == "English"]

            
import matplotlib.pyplot as plt

#plt.plot(stats.length, stats.unique, "bo")
#plt.loglog(stats.length, stats.unique, "bo")

plt.figure(figsize = (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")
