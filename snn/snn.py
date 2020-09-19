import numpy as np
import csv
import math
import tensorflow as tf
from tensorflow import keras
import time
from sklearn.model_selection import train_test_split

## import training data and labels from file

training_data = []
training_labels = []        
        
with open('snn/data/train_data.csv') as csvfile:
 rdr = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
 for row in rdr:
  training_data.append(row)

with open('snn/data/train_labels.csv') as csvfile:
 rdr = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
 for row in rdr:
  training_labels.append(row)
        
train_data = np.asarray(training_data) 
train_labels = np.asarray(training_labels) 
        
print(len(train_data), len(train_labels))

input_layer_len = len(train_data[0])

x_train, x_test, y_train, y_test = train_test_split(train_data, train_labels, test_size=0.2, random_state=4)

print(len(x_train), len(y_train))
print(len(x_test), len(y_test))

# ## create and train model

input_layer_len = len(train_data[0])

model = keras.Sequential([
 keras.layers.Dense(input_layer_len, activation=tf.nn.relu),
 keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 # keras.layers.Dense(2000, activation=tf.nn.relu),
 keras.layers.Dense(11, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['sparse_categorical_accuracy'])
 # metrics=['accuracy']) 
 #accuracy has a bug where the loaded saved model loses accuracy


model.fit(x_train, y_train, epochs=5)

model.save("snn/models/snn-1.h5", overwrite=True, include_optimizer=True, save_format=None, signatures=None, options=None)

