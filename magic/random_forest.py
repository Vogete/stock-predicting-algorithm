from __future__ import division
import pandas as pd
import numpy as np
import pickle
from data_preprocessing import read_csv
from sklearn.ensemble import RandomForestClassifier

train_x, train_y, test_x, test_y = pickle.load(open("training_data.pickle","rb"))

X = [[0, 0], [1, 1]]
Y = [[0, 1, 0], [1, 1, 1] ]

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
