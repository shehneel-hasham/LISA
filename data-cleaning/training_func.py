import LSTM
import torch
import torch.nn as nn

def train(neural_net, x_int, y_int, epochs=10, batch_size=32, loss_rate=0.001, clip_value=1):
    
    # takes in parameters on the neural net, this is a pytorch thing
    optimiser = torch.optim.Adam(neural_net.parameters(), lr=loss_rate)

    loss_criterion = nn.CrossEntropyLoss()

    # sets the neural_net module in training mode
    # this is equivalent to neural_net.eval() or neural_net.train(mode=False)
    neural_net.train()

    # object representing the device in which torch.Tensor is allocated:
    device = torch.device("cpu")

    epoch_counter = 0

    for _ in range(0, epochs):

        epoch_counter += 1

        # initialise using function in LSTM
        hidden = neural_net.initialiseTensors(batch_size)

        for x, y in LSTM.get_batches(x_int, y_int, batch_size):

            # backpropagation

            # convert into torch tensor
            # input_tensor, target_tensor = torch.from_numpy(x), torch.from_numpy(y)
            input_tensor = torch.from_numpy(x).to(device).long()
            target_tensor = torch.from_numpy(y).to(device).long()

            # "detach" hidden state so that the gradient is not calculated using it
            # hence the neural net is not learning from the hidden state
            # if this isn't done then the gradients will be exploding or vanishing
            hidden = [hid.detach() for hid in hidden]

            # set gradients of all parameters to zero
            neural_net.zero_grad()

            # from LSTM module, using nn package
            output, hidden = neural_net(input_tensor, hidden)

            # tensor.view(-1) is used here to flatten (reshape) the tensor 
            loss = loss_criterion(output, target_tensor.view(-1))

            loss.backward()

            nn.utils.clip_grad_norm_(neural_net.parameters(), clip_value)

            # update the weights
            optimiser.step()

            if epoch_counter % 32:
                print(f"Epoch: {epoch_counter} of {epochs}\nLoss: {loss}\n")