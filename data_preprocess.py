import os
import nibabel as nib
import numpy as np
from PIL import Image

def convert_all_nii_to_jpg(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    nii_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".nii") or f.endswith(".nii.gz")])

    global_index = 1  

    for nii_file in nii_files:
        nii_path = os.path.join(input_dir, nii_file)
        img = nib.load(nii_path)
        volume = img.get_fdata()  # shape: (H, W, D)
        volume = np.transpose(volume, (2, 0, 1))  # 轉成 (D, H, W)

        for slice_2d in volume:
            # Normalize 到 0–255
            slice_2d = slice_2d - np.min(slice_2d)
            slice_2d = (slice_2d / (np.max(slice_2d) + 1e-5)) * 255
            slice_2d = slice_2d.astype(np.uint8)

            img_pil = Image.fromarray(slice_2d)
            save_path = os.path.join(output_dir, f"{global_index}_B.jpg")
            img_pil.save(save_path)
            global_index += 1

    print(f" 所有切片已儲存至 {output_dir}，共 {global_index - 1} 張圖像")


convert_all_nii_to_jpg(
    input_dir="./simple_data_3/val_ct",       # .nii 資料夾
    output_dir="./simple_cbct_ct_490/valB"    # 輸出的 jpg 資料夾
)
