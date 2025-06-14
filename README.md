# CycleGAN-CBCT_to_CT
This project uses a CycleGAN-based architecture to perform unpaired image-to-image translation from Cone Beam CT (CBCT) images to standard CT images.  
It is designed for medical image preprocessing and domain adaptation in radiotherapy.  

## Download Dataset
This project uses the CBCT Liver and Liver Tumor Segmentation Train/Test Data dataset available on Kaggle.  
You can download it manually from Kaggle at the following link:

🔗 [CBCT Liver and Liver Tumor Segmentation Train Data (Kaggle)](https://www.kaggle.com/datasets/maximiliantschuchnig/cbct-liver-and-liver-tumor-segmentation-train-data)  
🔗 [CBCT Liver and Liver Tumor Segmentation Test Data (Kaggle)](https://www.kaggle.com/datasets/maximiliantschuchnig/cbct-liver-and-liver-tumor-segmentation-test-data)

## Dataset Pre-processing
To convert 3D CBCT/CT volumes (`.nii`) into 2D images for training, run the data_preprocessing.py  
📌 Note: Replace input_dir and output_dir with the actual paths where your CBCT/CT data is stored and where you want the 2D images to be saved.

## Dataset Structure
After preprocessing, the CBCT and CT data are organized into a folder structure compatible with CycleGAN training:
```
cbct_ct/
├── trainA/   # CBCT training images
├── trainB/   # CT training images
├── valA/     # CBCT validation images
├── valB/     # CT validation images
├── testA/    # CBCT test images
└── testB/    # CT test images
```
📌 Note: All images are 2D grayscale .jpg slices. 

## train/test model
- Train a model:
```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot ./datasets/cbct_ct --name maps_cyclegan --model cycle_gan
```
To see more intermediate results, check out `./checkpoints/maps_cyclegan/web/index.html`.
- Test the model:
```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot ./datasets/cbct_ct --name maps_cyclegan --model cycle_gan
```
- The test results will be saved to a html file here: `./results/maps_cyclegan/latest_test/index.html`.


