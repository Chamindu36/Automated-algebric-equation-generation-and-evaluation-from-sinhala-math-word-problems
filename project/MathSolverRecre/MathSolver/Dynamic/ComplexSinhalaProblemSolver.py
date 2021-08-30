import csv
import nltk

from project.MathSolverRecre.constants import MainPath

nltk.download('perluniprops')
import nltk
nltk.download('state_union')
from keras.layers import Dropout, Dense
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import to_categorical
import numpy as np

from project.MathSolverRecre.MathSolver.Dynamic import SinhalaAlgebraProblems, PrepareSinhalaDataset
from project.MathSolverRecre.MathSolver.Dynamic.FetchProblem import fetch_problem
from project.MathSolverRecre.MathSolver.Dynamic.PrepareSinhalaDataset import sinhala_process

AlgebraSetPath = MainPath + "project/MathSolverRecre/MathSolver/AlgebraResources/Test2.csv"

def defineModelandOptimizer(top_words=0, max_length=0, ninputs=785):
    model = Sequential()
    # #Extra Layers
    # embedding_size: int = 8
    # num_words = 10000
    # num_tokens = 255
    # max_tokens = np.mean(num_tokens) + 2 * np.std(num_tokens)
    # model.add(Embedding(input_dim=num_words,
    #                 output_dim=embedding_size,
    #                 input_length=max_tokens,
    #                 name='layer_embedding'))
    # model.add(GRU(units=16, return_sequences=True))
    # model.add(GRU(units=8, return_sequences=True))
    # model.add(GRU(units=4))
    # #Mandatory layers
    model.add(Dense(30, input_dim=ninputs, activation='sigmoid'))
    model.add(Dropout(0))
    model.add(Dense(128, activation='softmax'))
    opt = SGD(lr=0.1)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def main(problem):
    global processed
    X = []
    Y = []
    topWords = 150
    maxProblemLength = 255
    # getting the data in the correct format, depending on which model we're using

    X, Y, words, prb = SinhalaAlgebraProblems.prepareAlgebraInput()

    print("X--------")
    print(X)
    print("Y-------------------------")
    print(Y)
    print("Words----------------------------")
    print(words)
    # pdb.set_trace()

    model = defineModelandOptimizer(top_words=topWords, max_length=maxProblemLength, ninputs=len(X[0]))
    model.fit(X, to_categorical(Y), epochs=300, batch_size=82, verbose=0)

    trueclass = []
    predclass = []
    processed = sinhala_process(problem)

    print("proceeed", processed)
    madeup = PrepareSinhalaDataset.makemap([processed[0]], words)
    print("Madeup:", madeup)
    X_test = np.array(madeup)

    print("XTest", X_test)

    nums = processed[1]
    problemType = list(model.predict(X_test))[0]
    words, nums, vars, subs = fetch_problem(problem)
    print("--------------------------------------")
    print(problemType)
    print("---------------------------------------")
    problemTypes = prb
    # pdb.set_trace()
    ans = problemTypes[problemType.tolist().index(max(problemType))]
    print("ans:", ans)

    print("This is Problem : ")
    print(words)
    print("Subjects in Question:")
    print(subs)
    print("Variables in Question:")
    print(vars)
    print("Numbers in Question:")
    print(nums)
    print("Looks like this is  {", ans, "} type problem")

csvf = open(AlgebraSetPath, 'r', encoding='utf16')
ans = list(csv.reader(csvf))

sent = "නයනිට ඇයගේ කැටය කැඩීමෙන් රුපියල් 5000 ක මුදලක් ලබා ගත්තාය. එහි කාසි වලින් තිබු මුදල මෙන් 4 ගුණයක් නෝට්ටු වලින් තිබුණි. කාසි වලින් හා නෝට්ටු වලින් ලැබුණු ගණන වෙන වෙනම සොයන්න "

main(sent)
