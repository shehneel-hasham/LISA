import numpy
import torch
import torch.nn as nn
import json

class LSTM(nn.Module):
    
    def __init__(self, dict, hidden=256, layers=4, dropout_prob=0.5, loss=0.001):
        super().__init__()

        self.hidden = hidden
        self.layers = layers
        self.dropout_prob = dropout_prob
        self.loss = loss

        # embedding layer is the first hidden layer in a nn
        # dict is the dictionary mapping of words to numbers
        self.vocab_size = len(dict)
        self.embed = nn.Embedding(self.vocab_size, 200)

        # lstm
        self.lstm = nn.LSTM(
            input_size=200, 
            hidden_size=self.hidden, 
            num_layers=self.layers, 
            dropout=dropout_prob, 
            batch_first=True
            )

        # dropout layer
        # regularises neurons and prevents co-adaptations of neurons
        self.dropout = nn.Dropout(dropout_prob)

        # connected layer
        self.fully_connected = nn.Linear(self.hidden, self.vocab_size)

    def forward(self, x, hidden):
        # running through neural net
        embed = self.embed(x)
        lstm_output, hidden_layer = self.lstm(embed, hidden)
        output = self.dropout(lstm_output)

        output = output.reshape(-1, self.hidden)

        output = self.fully_connected(output)

        return output, hidden_layer

    def initialiseTensors(self, batch_size):
        """
        Initialise the tensor for the hidden layer
        """
        return (torch.zeros(self.layers, batch_size, self.hidden),
                torch.zeros(self.layers, batch_size, self.hidden))

# loading the dictionary
try:
    with open("data/int2token.json", mode="r") as file:
        int2token = json.load(file)
except FileNotFoundError:
    print("Please run data_cleaning.py to generate int2token.json before continuing")

# testing LSTM infrastructure with dictionary
net = LSTM(int2token)
print(net)