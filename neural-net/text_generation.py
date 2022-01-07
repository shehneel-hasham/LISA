import torch
from data_cleaning import LSTM
# TODO sort out the file imports
# TODO check this works!!
# TODO delete all unused code
# TODO train neural-net on all data

LSTM_model = torch.load("../data-cleaning/data/trained/trained_model")
model = LSTM()
model.load_state_dict(LSTM_model["training_func_state_dict"])
print(model)

# # don't think I need this, delete the saving too 
# optimiser = torch.load("../data-cleaning/data/trained/trained_model")
# # need to find optimiser_class
# optimiser_class.load_state_dict(optimiser)