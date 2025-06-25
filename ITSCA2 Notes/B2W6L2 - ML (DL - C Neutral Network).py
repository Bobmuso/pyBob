import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator #covert and rescale image into dataset for training
from tensorflow.keras.models import Sequential #generate models
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense #image processing
from sklearn.metrics import classification_report, confusion_matrix

trainDir = 'catdog/training_set/'
testDir = 'catdog/testing_set/'

#prevent overfitting
trainDatagen = ImageDataGenerator(rescale =1./255, shear_ranging = 0.2, zoom_range = 0.2, horizontal_flip = True)
#prep data for training
trainGen = trainDatagen.flow_from_directory(trainDir, target_size = (64, 64), batch_size = 32, class_mode = 'binary')

testDatagen = ImageDataGenerator(rescale =1./255)
testGen = testDatagen.flow_from_directory(testDir, target_size = (64, 64), batch_size = 32, class_mode = 'binary')

trainImages, trainLabels = next(trainGen)
plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(trainImages[i])
    plt.xlabel('Cat' if trainLabels[i] == 0 else 'Dog')
plt.show()

#Build model
cnn = Sequential()
cnn.add(Conv2D(filters = 32, kernel_size = 3, activation = 'relu', input_shape = (64, 64, 3)))
cnn.add(MaxPooling2D(pool_size = 2, strides = 2))
cnn.add(Conv2D(filters = 32, kernel_size = 3, activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = 2, strides = 2))
cnn.add(Flatten())
cnn.add(Dense(units = 128, activation = 'relu'))
cnn.add(Dense(units = 1, activation = 'sigmoid'))
cnn.compile(optimizer = 'adam', loss = 'binary_crossentary', metrics = ['accuracy'])

#Train model
cnnTrained = cnn.fit(trainGen, epochs = 10, validation_data = testGen)
cnn.save('cnnModelCatsDogs.h5')

#y predict
yPred = cnn.predict(testGen)
yPredClass = (yPred > 0.5).astype('int32').flatten()
yActual = trainDatagen.classes

classRept = classification_report(yActual, yPredClass, target_names = ['Cat', 'Dog'])
print(classRept)

confMatrix = confusion_matrix(yActual, yPred, yPredClass)

plt.plot(cnnTrained.history['accuracy'], label = 'accuarcy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.show()
