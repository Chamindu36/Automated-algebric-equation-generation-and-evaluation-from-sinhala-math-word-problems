import numpy as np
from keras import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

from project.MathSolverRecre.MathSolver.RuleBased.SimpleProbModule.SimpleProbSolve import solve_simple_prob
from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareDataSet import preprocess_sinhala, make_map
from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareForANN import prepare_ANN_Simple


def define_Modeland_Optimizer(top_words=0, max_length=0, ninputs=785):
    model = Sequential()

    model.add(Dense(30, input_dim=ninputs, activation='sigmoid'))
    model.add(Dropout(0))
    model.add(Dense(8, activation='softmax'))
    opt = SGD(lr=0.1)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def simple_Problem_Classify(problem):
    global processed
    X = []
    Y = []
    topWords = 150
    maxProblemLength = 255

    # getting the data in the correct format, depending on which model we're using
    X, Y, words,types = prepare_ANN_Simple()
    print("X--------")
    print(X)
    print("Y-------------------------")
    print(Y)
    print("Words----------------------------")
    print(words)
    # pdb.set_trace()

    model = define_Modeland_Optimizer(top_words=topWords, max_length=maxProblemLength, ninputs=len(X[0]))
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
    answer = solve_simple_prob(ans,nums)
    print(answer)
    return problem,answer



