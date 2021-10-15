import tensorflow as tf

# mnist= tf.keras.datasets.mnist

# (x_train,y_train),(x_test,y_test)= mnist.load_data()
import numpy as np

import tensorflow as tf

# !pip install -q tensorflow-hub
# !pip install -q tfds-nightly
# import tensorflow_hub as hub
import tensorflow_datasets as tfds


print("Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
# print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")