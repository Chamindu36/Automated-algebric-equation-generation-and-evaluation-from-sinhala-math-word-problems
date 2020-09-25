import csv
import pdb
from decimal import Decimal
from fractions import Fraction

import nltk

from project.MathSolverRecre.Preprocessing.Tagger.TaggerUse import sentence_tag_in_array_style
from project.MathSolverRecre.Preprocessing.Utils.PrepareData import prepare_data
from project.MathSolverRecre.Preprocessing.Utils.Tokenizer import tokenize_texts

nltk.download('perluniprops')

import operator

import numpy as np
from nltk.tokenize.moses import MosesDetokenizer


def sinhala_process(s):
    nums = []
    # Tokenize the words from given sentence
    words = tokenize_texts(s)
    numcounter = 1
    # POS tagging sentence
    tagged = sentence_tag_in_array_style(s)

    # Process tagged data
    words, numcounter, nums ,tagged = prepare_data(words, numcounter, nums, tagged, True)

    return [words, nums]


def popularPhrases(strings, nWords, minRepeats):
    words = dict()
    phrasesinsamesentence = set()
    # print("thastrings into account:",strings)
    # pdb.set_trace()
    for problem in strings:
        phrasesinsamesentence.clear()
        for j in range(0, len(problem) - nWords + 1):
            phraseList = [problem[j]]
            # print(phrase)
            for k in range(1, nWords):
                phraseList.append(problem[j + k])
            detoken = MosesDetokenizer()
            phrase = detoken.detokenize(phraseList, return_str=True)
            # print(phrase)
            if (phrase not in phrasesinsamesentence) and (phrase[0].isdigit() is False) and phrase[0] != "(":
                phrasesinsamesentence.add(phrase)
                if (phrase not in words):
                    words[phrase] = 1
                else:
                    words[phrase] = words[phrase] + 1
    sortedList = (sorted(words.items(), key=operator.itemgetter(1)))
    # print(sortedList)
    ct = len(sortedList) - 1
    ans = []
    while (sortedList[ct][1] >= minRepeats and ct >= 0):
        # print(ct)
        ans.append(sortedList[ct][0])
        ct -= 1
    # print(ans)
    return ans


def initializeWordsList(strings):
    # for arithmetic, 9,5,5,4,3
    wdlst = (popularPhrases(strings, 1, 20) + popularPhrases(strings, 2, 10) + popularPhrases(strings, 3,
                                                                                              9) + popularPhrases(
        strings, 4, 8) + popularPhrases(strings, 5, 7))
    # pdb.set_trace()
    # print("wordlist: ", wdlst)
    return wdlst


def getanswers(corpus):
    answers = []
    for i in corpus:
        if i[2] == "Addition":
            answers.append(0)
        if i[2] == "Subtraction":
            answers.append(1)
        if i[2] == "Multiplication":
            answers.append(2)
        if i[2] == "Division":
            answers.append(3)
    return answers


def makemap(strs, wordslist):
    # pdb.set_trace()
    ans = []
    for i in strs:
        detoken = MosesDetokenizer()
        str = detoken.detokenize(i, return_str=True)
        # print(str)
        onehotmap = []
        for j in wordslist:
            if j in str:
                onehotmap.append(1)
            else:
                onehotmap.append(0)
        ans.append(onehotmap)
    return ans


def load_ANN():
    corpus = []
    f = list(csv.reader(
        open("D:/ZZ__FYP/project/MathSolverRecre/MathSolver/AlgebraResources/Test2.csv"
             )))
    for i in f:
        if (i[1] == "Arithmetic" and (
                i[2] == "Addition" or i[2] == "Subtraction" or i[2] == "Division" or i[2] == "Multiplication")):
            processed = sinhala_process(i[0])
            corpus.append([processed[0], i[1], i[2], processed[1]])
    strings = [row[0] for row in corpus]
    print("stirngs: ", strings)
    # pdb.set_trace()
    wordslist = initializeWordsList(strings)
    # pdb.set_trace()
    print(wordslist)
    X = makemap(strings, wordslist)
    X = np.array(X)
    Y = np.array(getanswers(corpus))
    print(X.tolist()[0].count(1))
    print("answers", getanswers(corpus))
    print("wordslist", wordslist)
    return X, Y, wordslist


sent = "කාමරයක අකිල මහතා දිග පළල මෙන් 2/3 කට වඩා මීටර x ප්‍රමාණයකින් අඩුය . කාමරයේ පළල 3 m වේ. එහි දිග දැක්වීමට x අඩංගු වීජීය ප්‍රකාශනයක් ලියන්න ."
sinhala_process(sent)
