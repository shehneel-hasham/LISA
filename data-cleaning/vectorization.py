import csv
from os import read
import numpy as np
import json

# vectorising the data set using one hot encoding
# TODO: skip-grams

# we have to pad sequences to make them equal length 

def create_sequence(text, len_seq = 5):
    sequences = []
    if len(text.split()) > len_seq:
        for i in range(len_seq, len(text.split())):
            seq = text.split()[i-len_seq:i+1]
            sequences.append(" ".join(seq))
        return sequences
    else:
        return text


def get_integer_seq(token2int, seq):
    return [token2int[w] for w in seq.split()]

sequences = []
with open('data/cleaned_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # next line done for use this later, don't reduce
    speeches = [[i for i in row] for row in reader]
    # hack to unnest a list
    speeches = sum(speeches, [])
    sequences = [create_sequence(speech) for speech in speeches]
    sequences = sum(sequences, [])
    # print the number of groups of 5 words
    print(len(sequences))
    # create inputs and targets (x and y)
    # eg if default len_seq = 5
    # the input would be the first 4 words of the sequence 
    # and the target would be the last 4 words of the sequence
    x = []
    y = []
    for sequence in sequences:
        x.append(" ".join(sequence.split()[:-1]))
        y.append(" ".join(sequence.split()[1:]))

    # creating an integer to token dictionary
    int2token = {}
    count = 0
    for speech in speeches:
        for w in set(speech.split()):
            int2token[count] = w
            count += 1
    token2int = {t: i for i, t in int2token.items()}
    # saving dictionaries for later
    # token2int:
    with open(file="data/token2int.json", mode="w") as file:
        json.dump(token2int, file, indent=4)
    with open(file="data/int2token.json", mode="w") as file:
        json.dump(int2token, file, indent=4)

    # convert text sequences to integer sequences
    x_int = [get_integer_seq(token2int, i) for i in x]
    y_int = [get_integer_seq(token2int, i) for i in y]
    # convert lists to numpy arrays
    x_int = np.array(x_int)
    y_int = np.array(y_int)
    np.savetxt("data/x_int.csv", x_int, delimiter=",")
    np.savetxt("data/y_int.csv", y_int, delimiter=",")