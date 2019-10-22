import tensorflow as tf
import numpy as np
import os
from keras.datasets import fish_foto_trainig_set

from keras.layers import *
from keras.activations import *
from keras.models import *
from keras.optimizers import *
from keras.initializers import *
from keras.utils.np_utils import to_categorical

from plotting import *

(x_train, y_train), (x_test, y_test) = fish_foto_trainig_set.load_data()

num_features = 5
train_size, test_size = x_train.shape[0], x_test.shape[0]

init_w = RandomUniform(minval=-0.5, maxval=0.5)
init_b = Constant(value=0.0)


model = Sequential()
model.add(Dense(16, kernel_initializer=init_w, bias_initializer=init_b, input_shape=(num_features,)))
model.add(Activation("relu"))
model.add(Dense(1, kernel_initializer=init_w, bias_initializer=init_b))
model.summary()