import tensorflow as tf
import time

#looking for availabel gpus
gpus = tf.config.list_physical_devices('GPU')
print("GPUs available:", gpus)

# v1 = tf.constant(5)
# v2 = tf.Variable(10)
#
# print(v1)
# print(v2)
#
# #checking mutability of the Variables
#
# v3 = tf.Variable(3)
# print("Before", v3)
#
# v3.assign(4)
# print("After", v3)

#Checking how much time is taken by tensorflow for this single variable
start = time.time()
a = tf.constant(5)
end = time.time()