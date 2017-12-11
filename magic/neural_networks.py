import tensorflow as tf
import numpy as np
import pickle
from data_preprocessing import read_csv

from tensorflow.examples.tutorials.mnist import input_data

pickles_to_load = [
    'training_data_0.pickle',
    'training_data_0-1000.pickle',
    'training_data_1000-2000.pickle',
    'training_data_2000-3000.pickle',
    'training_data_3000-4000.pickle',
    'training_data_4000-5000.pickle',
    'training_data_5000-6000.pickle',
    'training_data_6000-7000.pickle',
    'training_data_7000-8000.pickle',
    'training_data_8000-9000.pickle',
    'training_data_9000-10000.pickle',
    'training_data_10000-11000.pickle',
    'training_data_11000-12000.pickle',
    'training_data_12000-13000.pickle',
    'training_data_13000-14000.pickle',
    'training_data_14000-15000.pickle',
    'training_data_15000-16000.pickle',
    'training_data_16000-17000.pickle',
    'training_data_17000-18000.pickle',
    'training_data_18000-19000.pickle',
    'training_data_19000-20000.pickle',
    'training_data_20000-21000.pickle',
    'training_data_21000-22000.pickle',
    'training_data_last.pickle'
]

featureset = []

for pickle_to_load in pickles_to_load:
    print 'pickle: ', pickle_to_load
    loaded_pickle = pickle.load(open(pickle_to_load, "rb"))
    # print '\n\n loaded_pickle[0] \n\n', loaded_pickle[0]
    print '\n\n len(loaded_pickle) \n\n', len(loaded_pickle)
    for feature in loaded_pickle:
        featureset.append(feature)

    print '\n\n len(featureset) \n\n', len(featureset)

print '\n\n final len(featureset) \n\n', len(featureset)

featureset = np.array(featureset)

test_size = 0.1
testing_size = int(test_size*len(featureset))

train_x = list(featureset[:,0][:-testing_size])
train_y = list(featureset[:,1][:-testing_size])

test_x = list(featureset[:,0][-testing_size:])
test_y = list(featureset[:,1][-testing_size:])


# Number of Nodes in Hidden Layer

n_nodes_hl1 = 1500
n_nodes_hl2 = 1500
n_nodes_hl3 = 1500

n_classes = 2
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

    n_epochs = 12

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

                _, c = sess.run([optimizer, cost], feed_dict = {x: batch_x, y: batch_y})

                epoch_cost += c
                i += batch_size

            print 'Epoch', epoch + 1, 'completed out of ', n_epochs, 'epoch cost: ', epoch_cost

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy:',accuracy.eval({x: test_x, y: test_y}))

train_neural_network(x)
