from data_cleaning.LSTM_class import LSTM
import predict
import torch
import json
# TODO write predict func
# TODO check this works with the predict func 
# TODO delete all unused code
# TODO retrain neural-net on some data
# TODO update file structure in python section
# TODO update readme 
# TODO streamlit!!
# note: streamlit might only work in a docker container

try:
    with open("data_cleaning/data/int2token.json", mode="r") as file:
        int2token = json.load(file)
except FileNotFoundError:
    print("Please run data_cleaning.py to generate int2token.json before continuing")

LSTM_model = torch.load("data_cleaning/data/trained/trained_model")
model = LSTM(int2token)
model.load_state_dict(LSTM_model["training_func_state_dict"])
print(model)

# generating next words




# # don't think I need this, delete the saving too 
# optimiser = torch.load("../data-cleaning/data/trained/trained_model")
# # need to find optimiser_class
# optimiser_class.load_state_dict(optimiser)

# TODO delete the saving of the optimiser in data_cleaning if it is not needed