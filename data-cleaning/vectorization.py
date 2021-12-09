import csv
from os import read
import numpy as np

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


def get_integer_seq(seq):
    return [token2int[w] for w in seq.split()]

sequences = []
with open('cleaned_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    sequences = [[create_sequence(i) for i in row] for row in reader]
    sequences = sum(sequences, [])
    print(len(sequences))
    # create inputs and targets (x and y)
    x = []
    y = []
    for s in sequences:
        x.append(" ".join(s.split()[:-1]))
        y.append(" ".join(s.split()[1:]))
#         Traceback (most recent call last):
#   File "vectorization.py", line 34, in <module>
#     x.append(" ".join(s.split()[:-1]))
# AttributeError: 'list' object has no attribute 'split'

    # creating an integer to token dictionary
    int2token = {}
    count = 0
    for row in reader:
        for w in set(" ".join(row)):
            int2token[count] = w
            count += 1
    token2int = {t: i for i, t in int2token.items()}
    print(token2int(0))

    # convert text sequences to integer sequences
    x_int = [get_integer_seq(i) for i in x]
    y_int = [get_integer_seq(i) for i in y]
    # convert lists to numpy arrays
    x_int = np.array(x_int)
    y_int = np.array(y_int)
    numpy.savetxt("x_int.csv", x_int, delimiter=",")
    numpy.savetxt("y_int.csv", y_int, delimiter=",")