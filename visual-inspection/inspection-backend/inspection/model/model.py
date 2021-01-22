import tensorflow as tf


model = tf.keras.applications.MobileNetV2(input_shape=None,
                                          include_top=True,
                                          weights='imagenet')