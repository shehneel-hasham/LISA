import LSTM
import torch
import torch.nn as nn

def train(neural_net, x_int, y_int, epochs=10, batch_size=32, loss_rate=0.001, clip_value=1):
    
    # takes in parameters on the neural net, this is a pytorch thing
    optimiser = torch.optim.Adam(neural_net.parameters(), lr=loss_rate)

    loss = nn.CrossEntropyLoss()

    epoch_counter = 0

    # sets the neural_net module in training mode
    # this is equivalent to neural_net.eval() or neural_net.train(mode=False)
    neural_net.train()

    for epoch in range(epochs):

        # initialise using function in LSTM
        hidden = neural_net.initialiseTensors(batch_size)

        for x, y in LSTM.get_batches(x_int, y_int, batch_size):

            epoch_counter += 1

            # backpropagation