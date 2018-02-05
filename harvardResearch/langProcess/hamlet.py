import os
import pandas as pd

title_num = 1
book_dir = "./Books"
hamlets = pd.DataFrame(columns = ["language","text"])
for language in os.listdir(book_dir)[1:]:
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            if title == "Hamlet.txt":
                inputfile = book_dir + "/" + language + "/" + author + "/" + title
                print(inputfile)
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

# language, text = hamlets.iloc[0]
# counted_text = count_words_fast(text)

# data = pd.DataFrame({
#     "word": list(counted_text.keys()),
#     "count": list(counted_text.values())
# })

# data["length"] = data["word"].apply(len)

# data.loc[data["count"] > 10,  "frequency"] = "frequent"
# data.loc[data["count"] <= 10, "frequency"] = "infrequent"
# data.loc[data["count"] == 1,  "frequency"] = "unique"

# sub_data = pd.DataFrame({
#     "language": language,
#     "frequency": ["frequent","infrequent","unique"],
#     "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
#     "num_words": data.groupby(by = "frequency").size()
# })

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })

    return(sub_data)

grouped_data = pd.DataFrame(columns=["language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
    print(i)
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    #print(sub_data)
    grouped_data = grouped_data.append(sub_data)
