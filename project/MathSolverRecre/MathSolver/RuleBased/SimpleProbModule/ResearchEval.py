import csv

import numpy as np
from keras import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.utils import to_categorical

from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareDataSet import preprocess_sinhala, \
    initialize_WordsList, make_map
from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareForANN import get_types_Simple
from project.MathSolverRecre.constants import MainPath


def model_def(top_words=0, max_length=0, ninputs=785):
    model = Sequential()

    model.add(Dense(30, input_dim=ninputs, activation='sigmoid'))
    model.add(Dropout(0))
    model.add(Dense(4, activation='softmax'))
    opt = SGD(lr=0.1)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def method1():
    SimpleAlgebraCorpusPath = MainPath +"project/MathSolverRecre/MathSolver/AlgebraResources/SimpleAlgebraProblems.csv"
    corpus = []
    typesArray = []
    typesAndIndexArray = []
    typeCounter = 0
    csvf = open(SimpleAlgebraCorpusPath, 'r', encoding='utf8')
    f = list(csv.reader(csvf))
    for i in f:
        if (len(i[0]) != 0):
            processed = preprocess_sinhala(i[0])
            print(processed)
            type = i[2]
            # Add different types to array

            if (type not in typesArray):
                typeTuple = [type, typeCounter]
                typesArray.append(type)
                typesAndIndexArray.append(typeTuple)
                typeCounter = typeCounter + 1

            corpus.append([processed[0], type, processed[2], i[5]])
    strings = [row[0] for row in corpus]
    # pdb.set_trace()
    # print("poisdihusgdu", len(strings))

    wordslist = initialize_WordsList(strings)
    # # pdb.set_trace()
    X = make_map(strings, wordslist)
    X = np.array(X)
    Z = get_types_Simple(corpus, typesAndIndexArray)
    print(Z)
    Y = np.array(Z)
    print(X.tolist()[0].count(1))
    print("answers", get_types_Simple(corpus, typesAndIndexArray))
    print(X.tolist()[0].count(1))
    return X, Y, wordslist, typesArray


def simple_Problem_Classify(problem):
    global processed
    X = []
    Y = []
    topWords = 150
    maxProblemLength = 255

    # getting the data in the correct format, depending on which model we're using
    X, Y, words, types = method1()
    print("X--------")
    print(X)
    print("Y-------------------------")
    print(Y)
    print("Words----------------------------")
    print(words)
    # pdb.set_trace()

    model = model_def(top_words=topWords, max_length=maxProblemLength, ninputs=len(X[0]))
    model.fit(X, to_categorical(Y), epochs=300, batch_size=82, verbose=0)

    trueclass = []
    predclass = []
    processed = preprocess_sinhala(problem)
    print("Proceeed", processed)
    madeup = make_map([processed[0]], words)
    print("Madeup:", madeup)
    X_test = np.array(madeup)

    print("XTest", X_test)

    nums = processed[2]
    problemType = list(model.predict(X_test))[0]
    print("--------------------------------------")
    print(problemType)
    print("---------------------------------------")
    problemTypes = types
    print(problemTypes)
    # pdb.set_trace()
    ans = problemTypes[problemType.tolist().index(max(problemType))]
    print(ans)
    print("This is Problem : " + problem)
    print("Looks like this is a", ans, "problem")
    print(nums)
    answer = solve(ans, nums)
    print(answer)


def solve(problemtype, nums):
    numbersArray = []
    temp1 = 0
    for i in nums:
        k = int(i)
        numbersArray.append(k)

    operations = str(problemtype)
    print(numbersArray, operations)

    if (operations == "ADD"):
        temp1 = numbersArray[0] + numbersArray[1]
    elif (operations == "SUB"):
        temp1 = numbersArray[0] - numbersArray[1]
    elif (operations == "MUL"):
        temp1 = numbersArray[0] * numbersArray[1]
    elif (operations[0] == "DIV"):
        temp1 = numbersArray / numbersArray[1]
    print(temp1)
    return temp1


prob = 'ඩොල්ෆින් පැයකට මාළු 7 අනුභව කරයි. ඩොල්ෆින් මසුන් 56 ක් අනුභව කරන තෙක් පැය කීයක් තිබේද'
# simple_Problem_Classify(prob)
