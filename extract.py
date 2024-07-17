import zipfile
import os

# Paths
zip_path = 'D:\\IIITD\\CUDA\\Course4\\image-segmentation-cuda-python\\Data.zip' # '/mnt/data/Data.zip'
extract_path = 'D:\\IIITD\\CUDA\\Course4\\image-segmentation-cuda-python\\data\\initial' # './data/'

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Data extracted successfully.")
