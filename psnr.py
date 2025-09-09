from PIL import Image
import numpy as np
import math

def calculate_psnr(img1_path, img2_path):
    # 使用Pillow读取图片
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    # 转换为numpy数组
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    
    # 检查图片是否成功读取
    if img1_array.size == 0 or img2_array.size == 0:
        print("无法读取图片，请检查路径是否正确")
        return
    
    # 确保两张图片尺寸相同
    if img1_array.shape != img2_array.shape:
        print("两张图片尺寸不一致，无法计算PSNR")
        return
    
    # 将图片转换为float32类型
    img1_array = img1_array.astype(np.float32)
    img2_array = img2_array.astype(np.float32)
    
    # 计算MSE(均方误差)
    mse = np.mean((img1_array - img2_array) ** 2)
    
    if mse == 0:
        return float('inf')
    
    # 最大像素值(8位图像为255)
    max_pixel = 255.0
    
    # 计算PSNR
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    
    return psnr

# 图片路径
img1_path = r"./gt_100.png"
img2_path = r"./pred_100.png"

# 计算PSNR
psnr_value = calculate_psnr(img1_path, img2_path)

if psnr_value is not None:
    print(f"PSNR值为: {psnr_value:.2f} dB")