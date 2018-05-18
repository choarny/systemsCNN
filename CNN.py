"""
File Name: CNN
Author: Ryan Cho
Implementation of Keras and Tensorflow
"""
from __future__ import print_function
import keras
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
import matplotlib.pylab as plt

batch_size = 128
num_classes = 10
epochs = 10

# input image dimensions
img_x, img_y = 28, 28
