import numpy as np
from keras import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.utils import to_categorical
from sklearn.model_selection import StratifiedKFold

from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareForANN import prepare_ANN_Complex


def define_Modeland_Optimizer(top_words=0, max_length=0, ninputs=785):
    model = Sequential()

    model.add(Dense(30, input_dim=ninputs, activation='sigmoid'))
    model.add(Dropout(0))
    model.add(Dense(215, activation='softmax'))
    opt = SGD(lr=0.1)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model


def evaluate():
    global processed
    X = []
    Y = []
    topWords = 150
    maxProblemLength = 53

    X, Y, words = prepare_ANN_Complex()

    # in testing mode, we use kfold cross validation
    print("X:", X)
    print("Y:", Y)
    print("Number of features", len(X[0]))
    true_classes = []
    predicted_classes = []

    kfold = StratifiedKFold(5, shuffle=True)
    trueclass = []
    predclass = []
    model = define_Modeland_Optimizer(ninputs=len(X[0]))
    for train, test in kfold.split(X, Y):
        # print("SHAPE", X.shape)
        model.fit(X[train], to_categorical(Y[train], 215), epochs=1000, batch_size=100, verbose=0)
        scores = model.evaluate(X[test], to_categorical(Y[test], 215), verbose=0)
        finalloss = model.evaluate(X[train], to_categorical(Y[train], 215), verbose=0)
        true_classes = Y[test].tolist()
        print(true_classes)
        trueclass = trueclass + true_classes
        predicted_classes = model.predict_classes(X[test], len(X[test])).tolist()
        print(predicted_classes)
        predclass = predclass + predicted_classes
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
        print("Validation Accuracy: " + str(finalloss[1] * 100))

    ct = 0
    for i in range(0, len(true_classes)):
        if (true_classes[i] == predicted_classes[i]):
            ct += 1
    print(ct, "out of", len(true_classes), "guesses are correct. That's an accuracy of",
          float(ct) / float(len(true_classes)))
    print("Number of features", len(X[0]))
    trueclass = np.array(trueclass)
    predclass = np.array(predclass)
    # trueclass = trueclass.flatten()
    # predclass = predclass.flatten()
    correctGuesses = 0
    wrongGuesses = 0
    for i in range(0, len(trueclass)):
        if (trueclass[i] != 0):
            if (predclass[i] == trueclass[i]):
                correctGuesses += 1
            else:
                wrongGuesses += 1
    print("Correct Guesses: " + str(correctGuesses))
    print("Wrong Guesses: " + str(wrongGuesses))
    # pdb.set_trace()

evaluate()