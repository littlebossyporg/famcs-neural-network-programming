import numpy
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import SGD

# Выполните базовую версию программы обучения сверточной нейронной сети распознавания изображений.
# Попытайтесь улучшить качество обучения сети путем изменения различных гиперпараметров.
# Сохраните обученую сверточную нейронную сеть распознавания изображений.

# Задаем seed для повторяемости результатов
numpy.random.seed(42)
# Загружаем данные
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# Размер мини-выборки
batch_size = 32
# Количество классов изображений
nb_classes = 10
# Количество эпох для обучения
nb_epoch = 30
# Нормализуем данные
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)
# Создаем последовательную модель
model = Sequential()
# Формирование вектора, отвечающего за размерность входных данных:
# либо (кол-во каналов, ширина, высота), либо (ширина, высота, кол-во каналов)
# (в зависимости от значения параметра "image_data_format" в файле keras.json)
shape_vector = X_train.shape[1:]
# Первый сверточный слой
model.add(Conv2D(32, (3, 3), padding='same', input_shape=shape_vector, activation='relu'))
# Второй сверточный слой
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
# Первый слой подвыборки
model.add(MaxPooling2D(pool_size=(2, 2)))
# Слой регуляризации Dropout
model.add(Dropout(0.25))
# Третий сверточный слой
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
# Четвертый сверточный слой
model.add(Conv2D(64, (3, 3), activation='relu'))
# Второй слой подвыборки
model.add(MaxPooling2D(pool_size=(2, 2)))
# Слой регуляризации Dropout
model.add(Dropout(0.25))
# Слой преобразования данных из 2D представления в плоское
model.add(Flatten())
# Полносвязный слой для классификации
model.add(Dense(512, activation='relu'))
# Слой регуляризации Dropout
model.add(Dropout(0.5))
# Выходной полносвязный слой
model.add(Dense(nb_classes, activation='softmax'))
# Задаем параметры оптимизации
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# Обучаем модель
model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch, validation_split=0.1, shuffle=True, verbose=1)
# Оцениваем качество обучения модели на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))
model_json = model.to_json()
json_file = open("mnist_model_7_1.json", "w")
json_file.write(model_json)
json_file.close()
model.save_weights("mnist_model_7_1.h5")

# Точность работы на тестовых данных: 78.14% при nb_epoch = 25 lr=0.01
# Скорость обучения lr=0.02 Точность работы на тестовых данных: 52.42%
# Скорость обучения lr=0.05 Точность работы на тестовых данных: 10.00%
# Скорость обучения lr=0.1 Точность работы на тестовых данных: 10.00%
# чем выше скорость тем ниже точность

# Количество эпох обучения nb_epoch = 15 Точность работы на тестовых данных: 75.41%
# Количество эпох обучения nb_epoch = 25 Точность работы на тестовых данных: 78.14%
# Количество эпох обучения nb_epoch = 30
# чем больше эпох обучения тем выше точность

# Количество слоев в сети
#

