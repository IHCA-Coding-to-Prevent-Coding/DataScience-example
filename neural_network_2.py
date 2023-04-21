import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader



class CA_LSTM(nn.Module):
    def __init__(self,input, hidden_size=100):
        super(CA_LSTM, self).__init__()
        self.hidden_size = 1000;
        self.len_datapoints = input.shape[0];
        print(input.shape)
        
        # self.lstm = nn.LSTM(input.shape[1], self.hidden_size, self.len_datapoints, batch_first=True)
        self.lstm = nn.LSTM(  6,32,20,batch_first=False,dtype=torch.float64)
        
        self.fc1 = nn.Linear(32, 16, dtype=torch.float64);
        self.fc2 = nn.Linear( 16, 8, dtype=torch.float64);
        self.fc3 = nn.Linear( 8, 1, dtype=torch.float64);
     
        self.relu = nn.ReLU()
        
    def forward(self, x):
        
     
      
        h0 = torch.zeros(20,20,32,dtype=torch.double).to(device=x.device)
        c0 = torch.zeros(20,20,32,dtype=torch.double).to(device=x.device)
        
       
        out, _ = self.lstm(x, (h0, c0))
        
        out = self.relu(self.fc1(out[:, -1, :]))
        out = self.relu(self.fc2(out))
        out = self.fc3(out)
        return out.squeeze()
    
    
    

# write code here \/
def split_data(inputs, labels, train_ratio = 0.70):

    train_end = int(inputs.shape[0] * train_ratio);
    
    ## look up how to do this in numpy
    # splice the liststrain_data = df1.loc[0 : training_size - 1]
    X_train = inputs[0:train_end];
    X_test = inputs[train_end:];
    Y_train = labels[0:train_end];
    Y_test = labels[train_end:];
    
    train_loader = DataLoader(X_train, batch_size=1, shuffle=True);
    test_loader = DataLoader(X_test, batch_size=1, shuffle=True);
    
    return train_loader, test_loader, Y_train, Y_test




if __name__ == "__main__":
    
    num_epochs = 3 # CHANGE THIS!!!!
    seq_length = 1 # CHANGE THIS!!!!

    inputs = np.load("data/data.npy");
    labels = np.load("data/labels.npy");

    train_loader, test_loader, Y_train, Y_test = split_data(inputs, labels);

    net = CA_LSTM(inputs);

    print(net);

    # Define your loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

    # Training loop
    for epoch in range(num_epochs):
        net.train()  # Set network to training mode
        train_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            optimizer.zero_grad()

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        print("Epoch {}, training loss: {}".format(epoch+1, train_loss / len(train_loader)))

        # Validation loop
        net.eval()  # Set network to evaluation mode
        val_loss = 0.0
        val_accuracy = 0.0
        with torch.no_grad():
            for i, data in enumerate(test_loader, 0):
                inputs, labels = data

                outputs = net(inputs)
                loss = criterion(outputs, labels)
                val_loss += loss.item()

                _, predicted = torch.max(outputs.data, 1)
                val_accuracy += (predicted == labels).sum().item()

        print("Epoch {}, validation loss: {}, validation accuracy: {}".format(epoch+1, val_loss / len(val_loader), val_accuracy / len(val_loader.dataset)))





