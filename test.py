import torch

# 检查CUDA是否可用
print("CUDA Available:", torch.cuda.is_available())

# 获取当前GPU的计算能力（若CUDA可用）
if torch.cuda.is_available():
    device = torch.cuda.current_device()
    print("GPU Device Name:", torch.cuda.get_device_name(device))
    print("GPU Compute Capability:", torch.cuda.get_device_capability(device))
    print("PyTorch支持的CUDA架构列表:", torch.cuda.get_arch_list())
else:
    print("PyTorch未检测到GPU支持！")