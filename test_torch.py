import torch

# Check if PyTorch is installed
print("PyTorch version:", torch.__version__)

# Check if CUDA (GPU) is available
print("CUDA available:", torch.cuda.is_available())

# If CUDA is available, print details
if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))
    print("Device count:", torch.cuda.device_count())
    print("Current device:", torch.cuda.current_device())