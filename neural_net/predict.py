import torch
import numpy as np

def predict_next(neural_net, token2int: dict, input_string: str, hidden_state=None):

    inputs = torch.from_numpy(np.array([[token2int[input_string]]]))

    hidden = tuple([hid.data for hid in hidden_state])

    output, hidden = neural_net(inputs, hidden)

    pass

def generate_next(neural_net, token2int:dict, size: int, sample_input="technology today"):

    # setting neural_net to eval mode
    neural_net.eval()

    # set batch size at initialisation to 1
    hidden = neural_net.initialiseTensors(1)

    # working with the sample input text:
    tokens = sample_input.split()

    # predicting using the initial input
    for token in tokens:
        predicted_token, hidden = predict_next(neural_net, token2int, token, hidden)
    tokens.append(predicted_token)

    # to predict the next words:
    for _ in range(size):
        predicted_token, hidden = predict_next(neural_net, token2int, tokens[-1], hidden)
        tokens.append(predicted_token)
    
    return " ".join(tokens)