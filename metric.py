import os
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

# image 資料夾路徑
image_dir = './results_unet_32/maps_cyclegan/test_latest/images'

psnr_values = []
mae_values = []
rmse_values = []
ssim_values = []

for filename in sorted(os.listdir(image_dir)):
    if filename.endswith('_fake_B.png'):
        base_name = filename.replace('_fake_B.png', '')
        fake_path = os.path.join(image_dir, f"{base_name}_real_A.png")  # Model 輸出 fack ct or #_real cbct
        real_path = os.path.join(image_dir, f"{base_name}_real_B.png")  # Ground truth CT

        if os.path.exists(real_path):
            fake_img = cv2.imread(fake_path, cv2.IMREAD_GRAYSCALE)
            real_img = cv2.imread(real_path, cv2.IMREAD_GRAYSCALE)

            if fake_img.shape != real_img.shape:
                print(f"Shape mismatch: {fake_path} vs {real_path}")
                continue

            # 轉成 float32 做準確計算
            fake_img = fake_img.astype(np.float32)
            real_img = real_img.astype(np.float32)

            # 計算指標
            psnr_val = psnr(real_img, fake_img, data_range=255)
            mae_val = np.mean(np.abs(real_img - fake_img))
            rmse_val = np.sqrt(np.mean((real_img - fake_img) ** 2))
            ssim_val = ssim(real_img, fake_img, data_range=255)

            psnr_values.append(psnr_val)
            mae_values.append(mae_val)
            rmse_values.append(rmse_val)
            ssim_values.append(ssim_val)
        else:
            print(f"Missing file: {real_path}")

# output
def summarize(name, values):
    print(f"{name} mean: {np.mean(values):.2f}, std: {np.std(values):.2f}")

if psnr_values:
    summarize("PSNR", psnr_values)
    summarize("MAE", mae_values)
    summarize("RMSE", rmse_values)
    summarize("SSIM", ssim_values)
else:
    print("No valid image pairs found.")
