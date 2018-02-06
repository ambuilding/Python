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


colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )

plt.legend(numpoints=1, loc = "upper left")
plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show()
