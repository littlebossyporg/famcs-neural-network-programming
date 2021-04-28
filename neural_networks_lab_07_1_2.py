import numpy
from keras.models import model_from_json
from keras.datasets import mnist
# Утилиты для работы с массивами
from keras.utils import np_utils
# Пакет для обработки пикчей
from PIL import Image

# Загрузите сохраненную сверточную нейронную сеть распознавания изображений.

# Загружаем данные об архитектуре сети из файла json
json_filename = "mnist_model_7_1.json"
with open(json_filename, "r") as json_file:
    loaded_model_json = json_file.read()
# Создаем модель на основе загруженных данных
model = model_from_json(loaded_model_json)
# Загружаем веса в модель
h5_filename = "mnist_model_7_1.h5"
model.load_weights(h5_filename)
# Перед использованием загруженной нейронной сети необходимо её скомпилировать
model.compile(loss="categorical_crossentropy", optimizer="SGD",
              metrics=["accuracy"])
# Вывести начальные характеристики нейросети
print(model.summary())