import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import make_dot

a = torch.randn(1, requires_grad=True, dtype=torch.float)
b = torch.randn(1, requires_grad=True, dtype=torch.float)

loss_fn = nn.MSELoss(reduction='mean')

optimizer = optim.SGD([a, b], lr=lr)

for epoch in range(n_epochs):
    yhat = a + b * x_train_tensor
    loss = loss_fn(y_train_tensor, yhat)

    loss.backward()

    optimizer.step()
    optimizer.zero_grad()

print(a, b)