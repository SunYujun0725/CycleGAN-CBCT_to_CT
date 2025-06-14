import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
from skimage.transform import resize

def load_and_normalize(image_path):
    img = iio.imread(image_path).astype(np.float32)

    # RGB image 的話就取單一個 channel
    if img.ndim == 3 and img.shape[2] == 3:
        img = img[:, :, 0]

    if img.max() > 1.0:
        img /= 255.0
    return img

def resize_to_match(img, ref_img):
    if img.shape != ref_img.shape:
        img = resize(img, ref_img.shape, preserve_range=True, anti_aliasing=True)
    return img

def generate_comparison_plot(cbct_path, ours_path, real_ct_path, output_path='comparison_output.png'):
    # 1. Load and normalize
    cbct = load_and_normalize(cbct_path)
    ours = load_and_normalize(ours_path)
    real = load_and_normalize(real_ct_path)

    # 2. Resize CBCT and Ours to match Real CT
    cbct = resize_to_match(cbct, real)
    ours = resize_to_match(ours, real)

    # 3. Compute absolute difference (error maps)
    cbct_ct_error = np.abs(cbct - real)
    ours_ct_error = np.abs(ours - real)

    # 4. Mask to show only valid area in Real CT
    mask = real > 0.1
    cbct_ct_error[~mask] = 0
    ours_ct_error[~mask] = 0

    # 5. Amplify for visualization
    stretch = 10.0
    cbct_ct_error *= stretch
    ours_ct_error *= stretch

    # 6. Define color scaling
    vmax = max(np.percentile(cbct_ct_error, 99), np.percentile(ours_ct_error, 99))

    # 7. Plot
    fig, axs = plt.subplots(1, 5, figsize=(20, 4))
    titles = ['CBCT', 'Ours', 'Real CT', 'CBCT - CT', 'Ours - CT']
    images = [cbct, ours, real, cbct_ct_error, ours_ct_error]

    for i in range(3):
        axs[i].imshow(images[i], cmap='gray')
        axs[i].set_title(titles[i], fontsize=14)
        axs[i].axis('off')

    for i in range(3, 5):
        im = axs[i].imshow(images[i], cmap='jet', vmin=0, vmax=vmax)
        axs[i].set_title(titles[i], fontsize=14)
        axs[i].axis('off')
        fig.colorbar(im, ax=axs[i], shrink=0.6)

    plt.tight_layout(rect=[0, 0, 1, 0.95]) 
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f" Comparison figure saved to: {output_path}")

# --- Entry Point ---
if __name__ == '__main__':
    # 228, 354, 474, 521, 634, 710
    cbct_path = '/home/sunyujun/pytorch-CycleGAN-and-pix2pix/results_unet_32/maps_cyclegan/test_latest/images/521_B_real_A.png'
    ours_path = '/home/sunyujun/pytorch-CycleGAN-and-pix2pix/results_unet_32/maps_cyclegan/test_latest/images/521_B_fake_B.png'
    real_ct_path = '/home/sunyujun/pytorch-CycleGAN-and-pix2pix/results_unet_32/maps_cyclegan/test_latest/images/521_B_real_B.png'
    output_path = 'comparison_result.png'

    generate_comparison_plot(cbct_path, ours_path, real_ct_path, output_path)
