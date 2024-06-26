# importing the image module from matplotlib library

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
!wget 'https://tractive.com/blog/wp-content/uploads/2016/04/puppy-care-guide-for-new-parents.jpg'
img = mpimg.imread('/content/dog.jpg')
type(img)
print(img)
img_plot = plt.imshow(img)
plt.show()
from PIL import Image
img = Image.open('/content/dog.jpg')
img_resized = img.resize((200, 200))
img_resized.save('dog_image_resized.jpg')
# displaying the image from numpy array

img_res = mpimg.imread('/content/dog_image_resized.jpg')
img_res_plot = plt.imshow(img_res)
plt.show()
# importing OpenCV library
import cv2
grayscale_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
grayscale_image.shape
from google.colab.patches import cv2_imshow
# displaying the image
cv2_imshow(grayscale_image)
# saving the grayscale image
cv2.imwrite('dog_grayscale_image.jpg', grayscale_image)
