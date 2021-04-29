from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

# Используйте предварительно обученную сеть VGG16 в Keras для распознавания своего изображения.

# load the model
model = VGG16()
# load an image from file
image = load_img('корабль.png', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes
yhat = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2] * 100))

# В качестве результатов выполнения работы нужно показать результаты распознавания
'''mountain_bike (98.98%) для велосипед.jpg'''
'''aircraft_carrier (72.90%) для корабль.png'''