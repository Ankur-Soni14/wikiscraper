import torch
import numpy as np

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = torch.Tensor.to("cuda")

tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:,1] = 0
print(tensor)