import functools
import operator
import re

from project.MathSolverRecre.Preprocessing.Utils.Tokenizer import tokenize_texts
from project.MathSolverRecre.constants import MainPath

stem_dictionary = MainPath + "project/MathSolverRecre/Preprocessing/Resources/New_Stem_Dictionary.txt"


# Convert tuples in to strings
def convert_tuples(tup):
    str = functools.reduce(operator.add, (tup))
    return str


# Get the sinhala dictionary
stem_dict = [(l.strip(), 'utf-8') for l in open(stem_dictionary, encoding='utf-8')]

# Stemming of the words
stem_array = []

for s in stem_dict:
    s = ''.join(s)
    s = s.split("\t")
    s[1] = s[1].strip("utf-8")
    temp = (s[0], s[1])
    stem_array.append(temp)


def stemming(text):
    tokens = tokenize_texts(text)

    for k in range(0, len(tokens)):
        for i in range(0, len(stem_array)):
            if (stem_array[i][0] == tokens[k]):
                tokens[k] = stem_array[i][1]
    return tokens


