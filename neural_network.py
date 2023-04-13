import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader

num_epochs = 3 # CHANGE THIS!!!!
seq_length = 1 # CHANGE THIS!!!!
data =  # DATA GOES HERE IN THEORY
#CHOOSE CHARS OF LSTM
input_size, hidden_size, len_datapoints, output_size = []

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, len_datapoints, output_size):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.len_datapoints = len_datapoints
        self.lstm = nn.LSTM(input_size, hidden_size, len_datapoints, batch_first=True)
        self.fc1 = nn.Linear(hidden_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, output_size)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        h0 = torch.zeros(self.len_datapoints, x.size(0), self.hidden_size).to(device=x.device)
        c0 = torch.zeros(self.len_datapoints, x.size(0), self.hidden_size).to(device=x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.relu(self.fc1(out[:, -1, :]))
        out = self.relu(self.fc2(out))
        out = self.fc3(out)
        return out.squeeze()
    
    
    
# write code here \/
def split_data(data, seq_length, train_ratio = 0.70):
    n_samples = len(data)
    n_train_samples = int(n_samples * train_ratio)
    X_train, y_train = [], []
    X_val, y_val = [], []
    for i in range(n_samples - seq_length):
        if i < n_train_samples:
            X_train.append(data[i:i + seq_length])
            y_train.append(data[i + seq_length])
        else:
            X_val.append(data[i:i + seq_length])
            y_val.append(data[i + seq_length])
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_val = np.array(X_val)
    y_val = np.array(y_val) 
    return X_train, y_train, X_val, y_val


net = LSTM(input_size, hidden_size, len_datapoints, output_size)


# Define your loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)


X_train, train_dataset, X_val, val_dataset = split_data(data, seq_length, )
# Define your training and validation data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

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
        for i, data in enumerate(val_loader, 0):
            inputs, labels = data

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            val_accuracy += (predicted == labels).sum().item()

    print("Epoch {}, validation loss: {}, validation accuracy: {}".format(epoch+1, val_loss / len(val_loader), val_accuracy / len(val_loader.dataset)))