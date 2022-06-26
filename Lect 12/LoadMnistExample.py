from tensorflow import keras
from keras.datasets import mnist
from matplotlib import pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
N = 400
img = test_images[N, ]
plt.imshow(img, interpolation='nearest')
plt.axis('off')
plt.show()

# It can be used to reconstruct the model identically.
reconstructed_model = keras.models.load_model("my_model_mnist")
reconstructed_model.summary()

# Let's check:
img1 = img.flatten()
x_test = test_images.reshape(10000, 784)
pred = reconstructed_model.predict(x_test)
print('prediction is', pred[N, ])
