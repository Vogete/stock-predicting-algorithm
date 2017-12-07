import tensorflow as tf
import numpy as np
import pickle
from data_preprocessing import read_csv

from tensorflow.examples.tutorials.mnist import input_data

# mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)
train_x, train_y, test_x, test_y = pickle.load(open("training_data.pickle","rb"))

print '\n\n type(train_x) \n\n', type(train_x)
print '\n\n type(train_x[0]) \n\n', type(train_x[0])
print '\n\n train_x \n\n', train_x
print '\n\n train_x[0] \n\n', train_x[0]

print '\n\n type(train_y) \n\n', type(train_y)
print '\n\n type(train_y[0]) \n\n', type(train_y[0])
print '\n\n train_y \n\n', train_y
print '\n\n train_y[0] \n\n', train_y[0]

# df_training_data = read_csv('../assets/training_data/training_data-stock_change-normalized.csv', ',')

# print df_training_data['stock_price_change'].head()

# Number of Nodes in Hidden Layer

n_nodes_hl1 = 1500
n_nodes_hl2 = 1500
n_nodes_hl3 = 1500

n_classes = 3
batch_size = 50

x = tf.placeholder('float', [None, len(train_x[0])])
y = tf.placeholder('float')

def neural_network_model(data):
    hidden_layer_1 = {'weights': tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_layer_2 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_layer_3 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases': tf.Variable(tf.random_normal([n_classes]))}

    l1 = tf.add(tf.matmul(data, hidden_layer_1['weights']), hidden_layer_1['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_layer_2['weights']), hidden_layer_2['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_layer_3['weights']), hidden_layer_3['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, output_layer['weights']), output_layer['biases'])

    print output
    return output

def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    optimizer = tf.train.AdamOptimizer().minimize(cost)

    n_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(n_epochs):
            epoch_cost = 0

            i = 0
            while i < len(train_x):
                start = i
                end = i + batch_size

                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])


                # print len(batch_x)
                # print len(batch_y)

                # print len(batch_x[0])
                # print len(batch_y[0])

                # print len(batch_x[1])
                # print len(batch_y[1])

                # print "TYPE batch_x[0] \n\n", type(batch_x)
                # print "\n batch_x[1] \n\n", batch_x[1]

                # print "batch_x[0] \n\n", batch_x[0]
                # print "\n batch_x[1] \n\n", batch_x[1]

                # print "batch_y[0] \n\n", type(batch_y[0])
                # print "\n batch_y[1] \n\n", batch_y[1]

                _, c = sess.run([optimizer, cost], feed_dict = {x: batch_x, y: batch_y})

                epoch_cost += c
                i += batch_size

            print 'Epoch', epoch, 'completed out of ', n_epochs, 'epoch cost: ', epoch_cost

            correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
            accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

            print 'accuracy: ', accuracy.eval({x: test_x, y: test_y})

train_neural_network(x)
