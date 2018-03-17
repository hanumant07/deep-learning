import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')


SEED = 7
numpy.random.seed(SEED)


def fetch_preprocess_data():
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    # reshape to channel x height x width
    X_train = X_train.reshape(X_train[0], 1, 28, 28).astype('float32')
    X_test = X_test.reshape(X_test[0], 1, 28, 28).astype('float32')

    # one hot encode output
    Y_train = np_utils.to_categorical(Y_train)
    Y_test = np_utils.to_categorical(Y_test)

    # rescale images
    X_train = X_train / 255
    X_test = X_test / 255
    return (X_train, Y_train), (X_test, Y_test)


def create_model(input_dim, output_dim):
    model = Sequential
    model.add(Conv2D(30, (5, 5), input_shape=input_dim, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(15, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(output_dim, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metric=['accuracy'])
    return model


def train_and_evaluate_model(model, X_train, Y_train, X_test, Y_test,
                             epochs, batch_size):

    model.fit(X_train, Y_train, validation_data=(X_test, Y_test),
              epochs=epochs, batch_size=batch_size, verbose=1)

    scores = model.evaluate(X_test, Y_test, verbose=0)
    print("CNN error: %.2f%%" % 100-scores[1]*100)


(X_train, Y_train), (X_test, Y_test) = fetch_preprocess_data()
model = create_model((1, 28, 28), 10)
train_and_evaluate_model(model, X_train, Y_train, X_test, Y_test, 30, 100)
