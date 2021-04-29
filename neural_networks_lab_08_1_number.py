import numpy as np
from keras.preprocessing import image
from tensorflow.python.keras.models import model_from_json

# Используйте обученные сверточные нейронные сети для распознавания своих объектов и рукописных цифр.
# Распознаю цифру 9 из 6 лабы

img_path = '9.png'
img = image.load_img(img_path, target_size=(28, 28), grayscale=True)
x = image.img_to_array(img)
x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)
json_file = open("mnist_model_7_3.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("mnist_model_7_3.h5")
loaded_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
prediction = loaded_model.predict(x)
print(np.argmax(prediction))

''' 9 '''
