import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
img=Image.open("girl.jpg")
matrix=np.array(img)
new_image=Image.fromarray(matrix)
plt.imshow(new_image)
plt.axis("off")
plt.show()