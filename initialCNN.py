import os
from PIL import Image

# Specify the path to the dataset folder
dataset_path = 'Desktop/dataset_FVC2000_DB4_B'

# Specify the path to the real_data folder
real_data_path = os.path.join(dataset_path, 'real_data')

# Loop over each image in the real_data folder and display it
for i in range(1, 801):
    # Construct the image filename
    image_filename = os.path.join(real_data_path, 'db4_b_' + str(i) + '.bmp')
    
    # Load the image using PIL
    image = Image.open(image_filename)
    
    # Display the image using PIL
    image.show()

