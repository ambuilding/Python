import numpy as np
from collections import Counter

def frequency(chars):
    frequencies     = dict(Counter(chars.values()))
    sum_frequencies = sum(frequencies.values())
    for key in frequencies:
        frequencies[key] /= sum_frequencies
    return frequencies


def chance_homophily(chars):
    frequencies = frequency(chars)
    return np.sum(np.square(list(frequencies.values())))

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)


import pandas as pd

df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df[df["village"] == 1]
df2 = df[df["village"] == 2]

sex1      = df1.set_index("pid")["resp_gend"].to_dict()
caste1    = df1.set_index("pid")["caste"].to_dict()
religion1 = df1.set_index("pid")["religion"].to_dict()

sex2      = df2.set_index("pid")["resp_gend"].to_dict()
caste2    = df2.set_index("pid")["caste"].to_dict()
religion2 = df2.set_index("pid")["religion"].to_dict()


print("Village 1 chance of same sex:", chance_homophily(sex1))
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))


def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)

# obtain the personal IDs for Villages 1 and 2
pid1 = pd.read_csv(data_filepath + "key_vilno_1.csv", header = None)
pid2 = pd.read_csv(data_filepath + "key_vilno_2.csv", header = None)

print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1), chance_homophily(sex1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1), chance_homophily(caste1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1), chance_homophily(religion1))

print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2), chance_homophily(sex2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2), chance_homophily(caste2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2), chance_homophily(religion2))
