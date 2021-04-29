import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json

# Используйте обученные сверточные нейронные сети для распознавания своих объектов и рукописных цифр.
# Распознаю кораблик с картинки корабль.png

json_file = open("mnist_model_7_1.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("mnist_model_7_1.h5")
loaded_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
print("Загрузили Model")
img_path = 'корабль.png'
img = image.load_img(img_path, target_size=(32, 32))
x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)
prediction = loaded_model.predict(x)
print(prediction)
classes = ['велосипед', 'автомобиль', 'птица', 'кот', 'олень', 'собака', 'лягушка', 'лошадь', 'корабль', 'грузовик']
print(classes[np.argmax(prediction)])

'''[[4.7443162e-08 3.5568984e-10 2.0953497e-09 1.2010206e-12 1.4315407e-11
  1.0075057e-13 1.2892323e-12 2.1419507e-11 9.9999988e-01 8.3762330e-08]]
корабль
'''