# CycleGAN-CBCT_to_CT

## Download Dataset
This project uses the CBCT Liver and Liver Tumor Segmentation Train/Test Data dataset available on Kaggle.  
You can download it manually from Kaggle at the following link:

🔗 [CBCT Liver and Liver Tumor Segmentation Train Data (Kaggle)](https://www.kaggle.com/datasets/maximiliantschuchnig/cbct-liver-and-liver-tumor-segmentation-train-data)  
🔗 [CBCT Liver and Liver Tumor Segmentation Test Data (Kaggle)](https://www.kaggle.com/datasets/maximiliantschuchnig/cbct-liver-and-liver-tumor-segmentation-test-data)

## Dataset Pre-processing
To convert 3D CBCT/CT volumes (`.nii`) into 2D images for training, run the data_preprocessing.py  
📌 Note:
Replace input_dir and output_dir with the actual paths where your CBCT/CT data is stored and where you want the 2D images to be saved.
