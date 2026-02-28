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
#v3 = tf.Variable(3)
# print("Before", v3)
#
# v3.assign(4)
# print("After", v3)

#Checking how much time is taken by tensorflow for this single variable
# start = time.time()
# a = tf.constant(5)
# end = time.time()


#started arithmatic operations in tenserflow

a = tf.constant(5)
b = tf.constant(3)

c = tf.add(a, b)
print("Addition:", c)


d = tf.subtract(a, b)
print("Subtraction:", d)


e = tf.multiply(a, b)
print("Multiplication:", e)


f = tf.divide(a, b)
print("Division:", f)