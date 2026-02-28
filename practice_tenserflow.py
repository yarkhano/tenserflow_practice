import tensorflow as tf

v1 = tf.constant(5)
v2 = tf.Variable(10)

print(v1)
print(v2)

#checking mutability of the Variables

v3 = tf.Variable(3)
print("Before", v3)

v3.assign(4)
print("After", v3)