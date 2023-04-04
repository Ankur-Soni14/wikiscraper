import torch
import numpy as np
from torch import torch.Tensor

# This computes the matrix multiplication between two torch.Tensors. y1, y2, y3 will have the same value
y1 = torch.Tensor @ torch.Tensor.T
y2 = torch.Tensor.matmul(torch.Tensor.T)

y3 = torch.rand_like(y1)
torch.matmul(torch.Tensor, torch.Tensor.T, out=y3)


# This computes the element-wise product. z1, z2, z3 will have the same value
z1 = torch.Tensor * torch.Tensor
z2 = torch.Tensor.mul(torch.Tensor)

z3 = torch.rand_like(torch.Tensor)
torch.mul(torch.Tensor, torch.Tensor, out=z3)