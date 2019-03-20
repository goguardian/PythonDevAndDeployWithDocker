#!/usr/bin/env python3

import keras
from keras.datasets import mnist
import pandas as pd
import numpy as np

def prepare_data():
    '''
    Loads and preprocesses the training data.
    Returns tuple of (x_train, y_train, x_test, y_test).
    '''
    # Load training and test data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Reshape training and test data
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    # Scale training and test data
    x_train = (x_train / 256).astype('float32')
    x_test = (x_test / 256).astype('float32')

    # One-hot encode training and test labels
    y_train = keras.utils.to_categorical(y_train, 10).astype('int')
    y_test = keras.utils.to_categorical(y_test, 10).astype('int')
    
    return x_train, y_train, x_test, y_test


def build_model(input_shape):
    '''
    Builds and returns a simple Keras MNIST model.
    '''
    # Instantiate the model
    model = keras.models.Sequential([
        keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=input_shape),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(64, (3,3), activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(32),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # Compile the model
    model.compile(optimizer=keras.optimizers.Adam(), \
                  loss=keras.losses.categorical_crossentropy, \
                  metrics=['accuracy'])
    
    # Print out the model summary
    print(model.summary())
    
    # Return the model
    return model

if __name__=="__main__":
    
    x_train, y_train, x_test, y_test = prepare_data()
    
    # Record the input shape
    input_shape = x_train[0].shape
    
    model = build_model(input_shape)

    # Train and evaluate the model
    history = model.fit(x_train, y_train, validation_split=0.1, \
                        batch_size=32, epochs=2)
    test_loss, test_acc = model.evaluate(x_test, y_test)

    print('The test set has a loss of {:0.3f} and an accuracy of {:0.3f}. Saving model...'.format(test_loss, test_acc))

    # Save the model
    model.save('../deployWithDocker/docker/model.h5')
