from LSTM import LSTM
import training_func
import json
import numpy as np

# loading the dictionary
try:
    with open("data/int2token.json", mode="r") as file:
        int2token = json.load(file)
except FileNotFoundError:
    print("Please run data_cleaning.py to generate int2token.json before continuing")

try:
    x_int = np.loadtxt("data/x_int.txt", delimiter=",")
except FileNotFoundError:
    print("Please run vectorization.py to generate x_int.txt before continuing")

try:
    y_int = np.loadtxt("data/y_int.txt", delimiter=",")
except FileNotFoundError:
    print("Please run vectorization.py to generate y_int.txt before continuing")

neural_net = LSTM(int2token)
print(neural_net)

training_func.train(neural_net=neural_net, x_int=x_int, y_int=y_int, epochs=10, batch_size=5)