import functools
import operator
import pickle

import nltk

from project.MathSolverRecre.Preprocessing.Stemmer.StopWordsFilter import get_Stop_Words, filter_text
from project.MathSolverRecre.Preprocessing.Tagger.PosPerceptronTagger import ngramTagger, training_corpus
from project.MathSolverRecre.Preprocessing.Utils.RemoveUnnecessaryChars import delete_punctuation

nltk.download('state_union')
from nltk.corpus import state_unionUTF

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "#", "...", "..", "-"]

testSetPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Book.txt"

sample_text = state_unionUTF.raw(testSetPath)
# print(train_text)

'NN	-	Noun  ' \
'NNP - Proper Noun' \
'PRP - Pronoun' \
'VAUX- Verb Auxiliary ' \
'JJ	-	Adjective ' \
'RB	-	Adverb' \
'RP	- Particle' \
'CC	-	Conjuncts' \
'VH	-	Interjection' \
'PREP- Postposition' \
'QF	-	Quantifiers' \
'QFNUM-Number' \
'VFM	-	Verb Finite math' \
'VJJ	-	Verb Non-Finite Adjectival' \
'VRB	-	Verb Non-Finite Adverbial ' \
'VNN	-	verb Non-Finite Nominal' \
'QW	-	Question words ' \
'NLOC	-	Noun Location ' \
'INTF	-	Intensifier' \
'NEG	-	Negative' \
'NNC	-	Compound Nouns' \
'NNPC	-	Compound Proper Nouns' \
'NVB , JVB , RBVB	-	Light verbs ' \
'SYM	-	Special' \
'DIV - Division keywords' \
'MUL - Multiplication Keywords' \
'ADD - Addition Keywords' \
'SUB - Substraction Keywords' \
'ATT - Attributes' \
'VAR -  Variable in English' \
'EXP - Algebric Expressions' \
'QNUM - Question Numbers '


def convert_tuples(tup):
    str = functools.reduce(operator.add, (tup))
    return str


stopWords = []
stopWords = get_Stop_Words()

# Unigram perceptron tagger Run
tagger_f = open("perceptron_tagger.pickle", "rb")
tagger = pickle.load(tagger_f)

# Trigran Tagger initiation
taggerNgram = ngramTagger(training_corpus, 3, "NNN")


def pos_tagging(sentence):
    # POS Tagging with Trigram Tagger
    tagged = (taggerNgram.tag(sentence))

    # pos Tagging with unigram tagger
    # tagged = (tagger.tag(sentence))

    # print(tagged)  # whole sentence
    posTaggedOutput = " ".join(word + "/" + tag for word, tag in tagged)

    return posTaggedOutput


def pos_tagging_array_type(sentence):
    # POS Tagging with Trigram Tagger
    outputTagged = []
    tagged = (taggerNgram.tag(sentence))
    for word, tag in tagged:
        set = [word, tag]
        output = tuple(set)
        outputTagged.append(output)
    return (outputTagged)


def pos_tagging_list_return(sentence):
    # POS Tagging with Trigram Tagger
    tagged = (taggerNgram.tag(sentence))

    # print(tagged)  # whole sentence
    posTaggedOutput = []
    for word, tag in tagged:
        taggedWord = word + "/" + tag
        posTaggedOutput.append(taggedWord)

    return posTaggedOutput


def pos_tagging_array_list_return(sentence):
    # POS Tagging with Trigram Tagger
    tagged = (taggerNgram.tag(sentence))

    # print(tagged)  # whole sentence
    posTaggedOutput = []
    for word, tag in tagged:
        taggedWord = []
        taggedWord.append(word)
        taggedWord.append(tag)
        posTaggedOutput.append(taggedWord)

    return posTaggedOutput


sentencess = []
with open(testSetPath, "r", encoding="utf-8") as sentences_file:
    for line in sentences_file:
        # remove linebreak which is the last character of the string
        statement = line[:-1]
        statement = filter_text(statement)
        statement = pos_tagging(statement)
        sentencess.append(statement)


# print(sentencess[2])

def sentence_tag(sentence):
    sents = []
    delete_punctuation(sentence)
    for line in sentence:
        statement = filter_text(line)
        statement = pos_tagging(statement)
        # print(statement)
        sents.append(statement)
    return sents


def sentence_tag_in_array_style(sentence):
    sents = []
    output = []
    # delete_punctuation(sentence)
    sentence = nltk.sent_tokenize(sentence)
    for line in sentence:
        statement = filter_text(line)
        statement = pos_tagging_array_type(statement)
        sents.append((statement))

    for i in sents:
        for j in i:
            output.append(j)
    return output


def clean_and_tag(path):
    with open(path, "r", encoding="utf-8") as sentences_file:
        # delete_punctuation(sentences_file)
        sents = []
        for line in sentences_file:
            # remove linebreak which is the last character of the string
            statement = line[:-1]
            statement = filter_text(statement)
            statement = pos_tagging(statement)
            # print(statement)
            sents.append(statement)
        print(sents)


clean_and_tag(testSetPath)
sentence_tag_in_array_style("පැන්සල සහ මකනයක්  සඳහා රුපියල් 15 ක් වැය වන අතර , පැන්සල් 2 ක් සහ මකන 3 ක් සඳහා රුපියල් 35 ක් වැය වේ. මකනයක සහ පැන්සලක මිල ගණනය කරන්න.")
