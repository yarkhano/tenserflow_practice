import tensorflow as tf

#matrix multiplicaion

m1 = tf.constant([[1,2,3],[2,3,4]])
m2 = tf.constant([[2,3,4],[5,6,7],[4,6,7]])
m3 = tf.matmul(m1,m2)
print(m3)


#Mini Practice Challenge
X = tf.constant([[2, 3]])
W = tf.constant([[1],
                 [4]])
b = tf.constant([5])

result = tf.matmul(X, W) + b
print(result)
