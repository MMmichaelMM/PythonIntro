# pip3 install Keras
# pip3 install Tensorflow

from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

import tensorflow as tf
from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(16, input_dim = 28 * 28, activation= 'relu'))
network.add(layers.Dense(16, activation = 'relu', input_shape=(16,)))
network.add(layers.Dense(10, activation = 'softmax'))

network.summary()

network.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)
network.save('my_model_mnist')


test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc, 'test_loss', test_loss)