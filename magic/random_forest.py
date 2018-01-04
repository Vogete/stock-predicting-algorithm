from __future__ import division
import pandas as pd
import numpy as np
import pickle
from data_preprocessing import read_csv
from sklearn.ensemble import RandomForestClassifier

pickles_to_load = [
    'training_data_-1000-0.pickle',
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

print featureset[0]

test_size = 0.1
testing_size = int(test_size*len(featureset))

train_x = list(featureset[:,0][:-testing_size])
train_y = list(featureset[:,1][:-testing_size])

test_x = list(featureset[:,0][-testing_size:])
test_y = list(featureset[:,1][-testing_size:])

# print train_x[1]
# print train_y[1]

clf = RandomForestClassifier(n_estimators = 10)
# clf = clf.fit(X, Y)
clf = clf.fit(train_x, train_y)

# print test_x[0]
# print test_y[0]



def convertArrayFloatToInt(array):
    intArray = []

    for element in array:
        intArray.append(int(element))

    return intArray



def prediction(_clf, _test_x, _test_y):
    correctPrediction = 0
    falsePrediction = 0

    for i, data in enumerate(test_x):
        answer =  clf.predict([data])

        prediction = answer[0]
        control = test_y[i]

        prediction = convertArrayFloatToInt(prediction)
        control = convertArrayFloatToInt(control)


        # print prediction
        # print control


        if prediction == control:
            correctPrediction += 1
            # print "equal"
        else:
            falsePrediction += 1
            # print "not"

        # print "-------------"

    ratio = correctPrediction / len(test_x)

    # print correctPrediction
    # print falsePrediction

    return ratio




precision = prediction(clf, test_x, test_y)

print precision
