import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
nosie = np.random.normal(0, 0.2, x_data.shape)
y_data = np.square(x_data)+nosie

x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

W_L1 = tf.Variable(tf.random_normal([1, 10]))
B_L1 = tf.Variable(tf.zeros([1, 10]))
L1 = tf.matmul(x, W_L1) + B_L1
O_L1 = tf.nn.tanh(L1)

W_L2 = tf.Variable(tf.random_normal([10,1]))
B_L2 = tf.Variable(tf.zeros([1, 1]))
L2 = tf.matmul(O_L1, W_L2) + B_L2
O_L2 = tf.nn.tanh(L2)

loss = tf.reduce_mean(tf.square(y - O_L2))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(2000):
        sess.run(train, feed_dict={x:x_data, y:y_data})

    prediction = sess.run(O_L2, feed_dict={x:x_data})

    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data, prediction, 'r-', lw=5)
    plt.show()
