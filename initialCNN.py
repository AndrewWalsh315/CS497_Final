import numpy as np
from PIL import Image

# Specify the path to the dataset folder
data_folder = 'path/to/fingerprint/dataset/folder'

# Initialize empty arrays to hold the images and corresponding labels
images = np.empty((800, 288, 384), dtype=np.uint8)
labels = np.empty((800,), dtype=np.int32)

# Loop over each image in the dataset folder and extract the image data and label
for i in range(1, 801):
    # Read the image data from file
    image_path = data_folder + '/DB4_B/' + str(i) + '.bmp'
    image = np.array(Image.open(image_path), dtype=np.uint8)
    
    # Add the image data to the images array
    images[i-1] = image
    
    # Extract the label from the image filename
    label = int((i-1)/8) + 1
    
    # Add the label to the labels array
    labels[i-1] = label
    
# Print the shape of the images and labels arrays
print('Images shape:', images.shape)
print('Labels shape:', labels.shape)
