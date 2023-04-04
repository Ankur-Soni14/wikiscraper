import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import make_dot


model = ManualLinearRegression().to(device)

print(model.state_dic())

loss_fn = nn.MSELoss(reduction='mean')
optimizer = optim.SGD(model.parameters(), lr=lr)

for epoch in range(n_epochs):

    model.train()

    yhat = model