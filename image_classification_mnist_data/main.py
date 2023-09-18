import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD
#from keras.utils import

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
