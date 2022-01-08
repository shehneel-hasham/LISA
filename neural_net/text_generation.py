from data_cleaning.LSTM_class import LSTM
import torch
import json
# TODO check this works!!
# TODO delete all unused code
# TODO train neural-net on some data
# TODO update readme and file structure

try:
    with open("data_cleaning/data/int2token.json", mode="r") as file:
        int2token = json.load(file)
except FileNotFoundError:
    print("Please run data_cleaning.py to generate int2token.json before continuing")

LSTM_model = torch.load("data_cleaning/data/trained/trained_model")
model = LSTM(int2token)
model.load_state_dict(LSTM_model["training_func_state_dict"])
print(model)

# # don't think I need this, delete the saving too 
# optimiser = torch.load("../data-cleaning/data/trained/trained_model")
# # need to find optimiser_class
# optimiser_class.load_state_dict(optimiser)