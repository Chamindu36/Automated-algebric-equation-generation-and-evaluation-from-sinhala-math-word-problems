import csv
import numpy as np
import operator
import math

import pandas as pd

from project.MathSolverRecre.MathSolver.Dynamic import PrepareSinhalaDataset
from project.MathSolverRecre.MathSolver.Dynamic.PrepareSinhalaDataset import sinhala_process
from project.MathSolverRecre.constants import MainPath

AlgebraSetPath = MainPath +"project/MathSolverRecre/MathSolver/AlgebraResources/Test2.csv"

def prepareAlgebraInput():
    csvf = open(AlgebraSetPath, 'r', encoding='utf16')
    ans = list(csv.reader(csvf))

    # print(len(ans))
    problems = []
    answers = []
    classes = []
    counter = 0
    # Create types of different Templates
    problemtypes = dict()
    problemtypelist = []

    # Count the number of problems in training set
    realprobcounter = 0

    # Process the problems
    for i in range(2, len(ans)):
        problem = ans[i]
        if (len(problem[0]) > 0):
            realprobcounter += 1
            # print(problem[0])

            # Append problems into an array
            problems.append(sinhala_process(problem[0]))
            # Check for the template
            if (len(problem[2]) != 0):
                answers.append([float(problem[1]), float(problem[2])])
            elif (len(problem[3]) != 0):
                answers.append([float(problem[1]), float(problem[2]), float(problem[3])])
            else:
                answers.append([float(problem[1])])
            # Check for template type of each problem
            problemtype = problem[4] + " " + problem[5]
            problemtypelist.append(problemtype)

            # Check repitition of each template
            if (problemtype not in problemtypes):
                problemtypes[problemtype] = 1
            else:
                problemtypes[problemtype] += 1
            # for the demo
            if (problem[4] == "m + n = a" and problem[5] == "m - n = b"):
                classes.append(1)
            else:
                classes.append(0)
    # Sorted_list is used to check frequency of a single template
    print("Problems List", sorted(list(problemtypes.values()), reverse=True))
    sorted_dict = sorted(problemtypes.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_dict)

    # Append template for the problems
    realclass = []
    for i in range(0, len(answers)):
        for j in range(0, len(answers[i])):
            if (answers[i][j] < 0 or math.floor(answers[i][j]) != answers[i][j]):
                continue;
    for i in range(0, len(problemtypelist)):
        # print(len(sorted_dict))
        boo = False
        for j in range(0, len(sorted_dict)):
            if (problemtypelist[i] == sorted_dict[j][0]):
                realclass.append(j + 1)
                boo = True
        if boo == False:
            realclass.append(0)
    # Create problems array
    questions = [row[0] for row in problems]
    print("Questions :", questions)
    print("Classes: ", classes)
    print("Answers", answers)
    print("RealClass", realclass)
    # print(len(realclass))
    # print(realprobcounter)
    print((problemtypelist))
    words = PrepareSinhalaDataset.initializeWordsList(questions)
    print("Words :", words)
    map = PrepareSinhalaDataset.makemap(questions, words)
    return np.array(map), np.array(realclass), words, problemtypelist



prepareAlgebraInput()
# write()