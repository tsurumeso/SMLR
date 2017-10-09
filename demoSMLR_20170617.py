# -*- coding: utf-8 -*-
'''
demoSMLR_20140714
'''

from __future__ import print_function

import matplotlib.pyplot as plt
import numpy
import sklearn.svm

import smlr


# Prepare classifier objects
svm = sklearn.svm.LinearSVC()
smlr = smlr.SMLR(max_iter=1000, tol=1e-5, verbose=1)

# Sample data generation

# Num of samples
N = 100

# Label vector
label4training = numpy.vstack((numpy.zeros((N, 1)), numpy.ones((N, 1))))
label4test = numpy.vstack((numpy.zeros((N, 1)), numpy.ones((N, 1))))

# Features
feature4class1 = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
feature4class2 = numpy.array([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

feature4training = numpy.vstack(((
    numpy.dot(numpy.ones((N, 1)), [feature4class1]),
    numpy.dot(numpy.ones((N, 1)), [feature4class2]))))
feature4test = numpy.vstack(((
    numpy.dot(numpy.ones((N, 1)), [feature4class1]),
    numpy.dot(numpy.ones((N, 1)), [feature4class2]))))

numpy.random.seed(seed=1)

feature4training = feature4training + \
    0.5 * numpy.random.randn(*feature4training.shape)
feature4test = feature4test + 0.5 * numpy.random.randn(*feature4test.shape)

# Scatter plot in the feature space
for n in range(len(label4training)):
    if label4training[n] == 0:
        plt.scatter(
            feature4training[n, 0], feature4training[n, 1], color='red')
    else:
        plt.scatter(
            feature4training[n, 0], feature4training[n, 1], color='blue')

plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()

# SMLR & SVM training
print("SMLR learning")
smlr.fit(feature4training, label4training)
print("SVM learning")
svm.fit(feature4training, label4training)

print("The SLMR weights obtained")
print(numpy.transpose(smlr.coef_))

# Linear boundary in the feature space
for n in range(len(label4training)):
    if label4training[n] == 0:
        plt.scatter(
            feature4training[n, 0], feature4training[n, 1], color='red')
    else:
        plt.scatter(
            feature4training[n, 0], feature4training[n, 1], color='blue')

plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
w = smlr.coef_[0, :]
x = numpy.arange(-5, 5, 0.001)
y = (-w[-1] - x * w[0]) / w[1]
plt.plot(x, y, color='black')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()

# generalization test
predictedLabelBySVM = svm.predict(feature4test)
predictedLabelBySMLR = smlr.predict(feature4test)

num_correct = 0
for n in range(len(label4test)):
    if label4test[n] == predictedLabelBySVM[n]:
        num_correct = num_correct + 1

svm_accuracy = numpy.double(num_correct) / len(label4test) * 100

num_correct = 0
for n in range(len(label4test)):
    if label4test[n] == predictedLabelBySMLR[n]:
        num_correct = num_correct + 1

smlr_accuracy = numpy.double(num_correct) / len(label4test) * 100

print("SVM accuracy: %s" % (svm_accuracy))
print("SMLR accuracy: %s" % (smlr_accuracy))
