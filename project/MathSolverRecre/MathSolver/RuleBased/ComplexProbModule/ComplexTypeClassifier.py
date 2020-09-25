import numpy as np
from keras.layers import Dropout, Dense
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import to_categorical
import nltk
nltk.download('perluniprops')

from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareDataSet import preprocess_sinhala, make_map
from project.MathSolverRecre.MathSolver.RuleBased.Utils.PrepareForANN import prepare_ANN_Complex


def define_Modeland_Optimizer(top_words=0, max_length=0, ninputs=785):
    model = Sequential()

    model.add(Dense(30, input_dim=ninputs, activation='sigmoid'))
    model.add(Dropout(0))
    model.add(Dense(5, activation='softmax'))
    opt = SGD(lr=0.1)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def complex_Problem_Classify(problem):
    global processed
    X = []
    Y = []
    topWords = 150
    maxProblemLength = 255

    # getting the data in the correct format, depending on which model we're using
    X, Y, words = prepare_ANN_Complex()
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
    problemTypes = ["Type01", "Type02", "Type03", "Type04", "Type05", "Type06"]
    # pdb.set_trace()
    ans = problemTypes[problemType.tolist().index(max(problemType))]
    print(ans)
    return ans


complex_Problem_Classify("නිමාලි සතුව නිල් පෑන් වලට වඩා රතු පෑන් 8 ක් ඇත. ඇය සතුව ඇති මුලු නිල් පෑන් සහ රතු පෑන් ගණන 20 ක් නම් නිල් පෑන් සහ රතු පෑන් ගණන වෙන වෙනම සොයන්න")
