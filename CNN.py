# Building CNN model
import tensorflow as tf
import keras
from keras.models import Model
from keras.models import Sequential
from keras.layers import Convolution1D, ZeroPadding1D, MaxPooling1D, BatchNormalization, Activation, Dropout, Flatten, Dense,SpatialDropout1D


def runCNN():
    pass
model = Sequential()
input_shape = (len(X_train[1]),1)
# First convolutional layer
''' 

'''
tf.random.set_seed(0)
model.add(Convolution1D(filters = 32, kernel_size=2, activation='relu', input_shape=input_shape ))
# Normalization batch
model.add(BatchNormalization())
# Max pooling 
# model.add(MaxPooling1D(pool_size=(2)))
model.add(Flatten())


# model.add(Dense(32, activation='tanh'))
# model.add(Dropout(0.2))
model.add(Dense(64, activation='tanh'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dense(100))
model.compile(optimizer='sgd',loss='mse', metrics=['mean_absolute_percentage_error'])
model.summary()

model.fit(X_train, y_train, epochs=100, verbose=2)