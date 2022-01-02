import numpy
import torch
import torch.nn as nn

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
        self.connected = nn.Linear(self.hidden, self.vocab_size)

    def forward(self, x, hidden):
        # running through neural net
        embed = self.embed(x)
        lstm_output, hidden_layer = self.lstm(embed, hidden)
        output = self.dropout(lstm_output)

        # TODO might error here because of reshape
        output = output.reshape(-1, self.hidden)

        output = self.connected(output)

        return output, hidden_layer

    def initialiseTensors(self, batch_size):
        pass
