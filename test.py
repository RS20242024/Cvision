import numpy as np
import matplotlib.pyplot as plt

image_array = np.random.rand(100, 100) * 255 
image_array = image_array.astype(np.uint8) # Ensure correct data type for image display
plt.imshow(image_array, cmap='gray') # 'gray' colormap for grayscale images
plt.colorbar() # Optional: add a color bar for intensity reference
plt.title("NumPy Array as Image")
plt.show()
