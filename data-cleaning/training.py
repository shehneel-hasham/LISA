from os import read
from LSTM import LSTM
import training_func
import json
import numpy as np
import torch

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

# rename this module!!! so confusing 
training_func.train(neural_net=neural_net, x_int=x_int, y_int=y_int, epochs=10, batch_size=64)
# torch.save(training_func, "data/trained_LSTM")
# checkpoint = {'state_dict': training_func.state_dict(),'optimizer' :optimizer.state_dict()}
# training_func.load_state_dict(checkpoint['model_state_dict'])
# optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
# epoch = checkpoint['epoch']
# loss = checkpoint['loss']

# model.eval()
torch.save({
    "training_func_state_dict": neural_net.state_dict(),
}, "data/trained/trained_model")
# with open("trained_LSTM") as file:
#     lines = file.read()
# optimizer = lines
# optimizer.load_state_dict(lines)