#Use model in another file
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

className = ['Cat', 'Dog']
cnn = load_model('cnnModelCatsDogs.h5')
img = load_img('dog_pic.jng', target_size = (64, 64))
imgArray = img_to_array(img)/255
testImage = np.expand_dims(imgArray, axis = 0)
predImage = cnn.predict(testImage)
predImageClass = 'Dog' if predImage[0] > 0.5 else 'Cat'

plt.imshow(load_img('dog_pic.png'))
plt.title(f'Predicted: {predImageClass}')
plt.axis('off')
plt.show()