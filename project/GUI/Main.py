# FYP

from project.MathSolverRecre.MathSolver.RuleBased.ComplexProbModule.SolveProblem import fetch_to_a_template
from project.MathSolverRecre.MathSolver.RuleBased.SimpleProbModule.SimpleTypeClassifier import simple_Problem_Classify
from project.MathSolverRecre.Preprocessing.Utils.ExtractDataFromPDF import readFile


def inteGratedSolve(filePath, isComplex):
    print(isComplex)
    outputArr = []

    if (isComplex is True):
        output = readFile(filePath)
        output = str(output)
        solved = fetch_to_a_template(output)
        print(solved)
        tuple1 = str("Question :\n" + output)
        outputArr.append(tuple1)
        tuple2 = str("Variables :\n" + str(solved[0]))
        outputArr.append(tuple2)
        tuple3 = str("Equations :\n" + str(solved[1]))
        outputArr.append(tuple3)
        tuple4 = str("Unit of Answer :\n " + str(solved[2]))
        outputArr.append(tuple4)
        tuple5 = str("Answers : \n" + str(solved[3]))
        outputArr.append(tuple5)

        return outputArr

    elif (isComplex is False):
        output = readFile(filePath)
        output = str(output)
        solved = simple_Problem_Classify(output)
        tuple1 = str("Question :\n"+ output)
        outputArr.append(tuple1)
        tuple2 = str("Answers : \n"+ str(solved[1]))
        outputArr.append(tuple2)
        return outputArr
