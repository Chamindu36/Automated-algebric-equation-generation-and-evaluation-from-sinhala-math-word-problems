from project.MathSolverRecre.MathSolver.RuleBased.ComplexProbModule.ComplexTypeClassifier import complex_Problem_Classify
from project.MathSolverRecre.MathSolver.RuleBased.ComplexProbModule.Smoothing.SmoothAndSlove import Smooth_Type_01, \
    Smooth_Type_02, Smooth_Type_03, Smooth_Type_04, Smooth_Type_05
from project.MathSolverRecre.MathSolver.RuleBased.ComplexTypes.Type_01 import Type01_solve
from project.MathSolverRecre.MathSolver.RuleBased.ComplexTypes.Type_02 import Type02_solve
from project.MathSolverRecre.MathSolver.RuleBased.ComplexTypes.Type_03 import Type03_solve
from project.MathSolverRecre.MathSolver.RuleBased.ComplexTypes.Type_04 import Type04_solve
from project.MathSolverRecre.MathSolver.RuleBased.ComplexTypes.Type_05 import Type05_solve
from project.MathSolverRecre.Preprocessing.Stemmer.Stemming import stemming
from project.MathSolverRecre.Preprocessing.Tagger.TaggerUse import sentence_tag_in_array_style
from project.MathSolverRecre.Preprocessing.Utils.PrepareData import prepare_data
from project.MathSolverRecre.Preprocessing.Stemmer.Stemming import stemming


def fetch_to_a_template(s):
    global duplicated
    print("Processing: " + s)

    nums = []
    mapped = list

    numcounter = 1
    s = s.replace(",", ".")

    words = stemming(s)
    tagged = sentence_tag_in_array_style(s)

    # Process tagged data
    words, numcounter, nums, tagged = prepare_data(words, numcounter, nums, tagged, False)

    type = complex_Problem_Classify(s)
    print(type)


    if(type == "Type01"):
        variablesReplace, finalExp, NNPI = Type01_solve(tagged, words)
        print("AFTER SMOOTHING : ---------------------------------------------------------")
        varArray, outPutExp, NNPI, answers = Smooth_Type_01(variablesReplace, finalExp, NNPI)

    elif(type == "Type02"):
        variablesReplace, finalExp, NNPI = Type02_solve(tagged, words)
        print("AFTER SMOOTHING : ---------------------------------------------------------")
        varArray, outPutExp, NNPI, answers = Smooth_Type_02(variablesReplace, finalExp, NNPI)

    elif(type == "Type03"):
        variablesReplace, finalExp, NNPI = Type03_solve(tagged, words)
        print("AFTER SMOOTHING : ---------------------------------------------------------")
        varArray, outPutExp, NNPI, answers = Smooth_Type_03(variablesReplace, finalExp, NNPI)

    elif(type == "Type04"):
        variablesReplace, finalExp, NNPI = Type04_solve(tagged, words)
        print("AFTER SMOOTHING : ---------------------------------------------------------")
        varArray, outPutExp, NNPI, answers = Smooth_Type_04(variablesReplace, finalExp, NNPI)

    elif (type == "Type05"):
        variablesReplace, finalExp, NNPI = Type05_solve(tagged, words)
        print("AFTER SMOOTHING : ---------------------------------------------------------")
        varArray, outPutExp, NNPI, answers = Smooth_Type_05(variablesReplace, finalExp, NNPI)


    return varArray, outPutExp, NNPI, answers

sent = "ගෙවත්තක ඇති මුලු අඹ ගස් සහ  පොල් ගස් ගණන 15 කි. එහි පොල් ගස් ගණන අඹ ගස් මෙන් 2 ගුණයකට වඩා 3 කින් වැඩිය. ගෙවත්තෙහි ඇති අඹ ගස් සහ  පොල් ගස් ගණන වෙන වෙනම සොයන්න "
fetch_to_a_template(sent)