import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import make_dot

torch.from_numpy(x_train)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

x_train_tensor = torch.from_numpy(x_train).float().to(device)
y_train_tensor = torch.from_numpy(y_train).flsoat().to(device)

print(type(x_train), type(x_train_tensor), x_train_tensor.type())