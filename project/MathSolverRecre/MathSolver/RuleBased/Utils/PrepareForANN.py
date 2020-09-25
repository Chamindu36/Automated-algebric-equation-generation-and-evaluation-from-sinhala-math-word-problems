import csv

import numpy as np

from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareDataSet import preprocess_sinhala, initialize_WordsList, make_map

SimpleAlgebraCorpusPath = "D:/ZZ__FYP/project/MathSolverRecre/MathSolver/AlgebraResources/SimpleAlgebraProblems.csv"
ComplexAlgebraCorpusPath = "D:/ZZ__FYP/project/MathSolverRecre/MathSolver/AlgebraResources/ComplexAlgebraDataset.csv"

def get_types_Simple(corpus, types):
    answers = []
    print(types)
    for i in corpus:
        for j in range(0,len(types)):
            if (i[1] == types[j][0]):
                answers.append(types[j][1])

    return answers


def get_types_Complex(corpus):
    answers = []
    for i in corpus:
        if i[1] == "Type01":
            answers.append(0)
        if i[1] == "Type02":
            answers.append(1)
        if i[1] == "Type03":
            answers.append(2)
        if i[1] == "Type04":
            answers.append(3)
        if i[1] == "Type05":
            answers.append(4)
        if i[1] == "Type06":
            answers.append(5)
    print(answers)
    return answers


def prepare_ANN_Simple():
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
            type = i[2] + "/" + i[3] + "/" + i[4]
            # Add different types to array

            if (type not in typesArray):
                typeTuple = [type, typeCounter]
                typesArray.append(type)
                typesAndIndexArray.append(typeTuple)
                typeCounter = typeCounter + 1

            corpus.append([processed[0], type, processed[2], i[5]])
    strings = [row[0] for row in corpus]
    # pdb.set_trace()
    wordslist = initialize_WordsList(strings)
    print(typesArray)
    # # pdb.set_trace()
    X = make_map(strings, wordslist)
    X = np.array(X)
    Y = np.array(get_types_Simple(corpus, typesAndIndexArray))
    print(X.tolist()[0].count(1))
    print("answers", get_types_Simple(corpus, typesAndIndexArray))
    print(X.tolist()[0].count(1))
    return X, Y, wordslist,typesArray


def prepare_ANN_Complex():
    csvf = open(ComplexAlgebraCorpusPath, 'r', encoding='utf8')
    f = list(csv.reader(csvf))
    corpus = []
    for i in f:
        if (i[1] == "Type01" or i[1] == "Type02" or i[1] == "Type03" or i[1] == "Type04" or i[1] == "Type05"):
            processed = preprocess_sinhala(i[0])
            corpus.append([processed[0], i[1], processed[2]])
    strings = [row[0] for row in corpus]
    # pdb.set_trace()
    # print("strings")
    wordslist = initialize_WordsList(strings)
    X = make_map(strings, wordslist)
    X = np.array(X)
    Y = np.array(get_types_Complex(corpus))
    print(X.tolist()[0].count(1))
    print("answers", get_types_Complex(corpus))
    print("wordslist", wordslist)
    return X, Y, wordslist


prepare_ANN_Simple()
