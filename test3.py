import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("Mnist_data", one_hot=True)
batch_size = 100
n_batch = mnist.train.num_examples//batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax(tf.matmul(x, W) + b)

loss = tf.reduce_mean(tf.square(y-prediction))
train = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for setp in range(n_batch):
            x_batch, y_batch = mnist.train.next_batch(batch_size)
            sess.run(train, feed_dict={x: x_batch, y: y_batch})

        acc = sess.run(accuracy, feed_dict={x: mnist.train.images, y: mnist.train.labels})
        print("Iter " + str(epoch) + ", Test Accuracy:  " + str(acc))

