import nltk
nltk.download('state_union')
from nltk.corpus import state_unionUTF

from project.MathSolverRecre.Preprocessing.Stemmer.Stemming import stemming


def get_Stop_Words():

    stopWordsPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/StopWords_425.txt"
    stopwords = [(l.strip(), 'utf-8') for l in open(stopWordsPath, encoding='utf-16')]

    StopWordsDic = []
    for word in stopwords:
        word = ''.join(word)
        word = word.split("\t")
        StopWordsDic.append(word[0])

    return StopWordsDic


def filter_text(sentence):
    stopWordsPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/StopWords_425.txt"
    stopwords = [(l.strip(), 'utf-8') for l in open(stopWordsPath, encoding='utf-16')]

    StopWordsDic = []
    for word in stopwords:
        word = ''.join(word)
        word = word.split("\t")
        StopWordsDic.append(word[0])

    # print(StopWordsDic)

    stemmedWords = stemming(sentence)
    # print(words)

    FilteredSentence = []
    for w in stemmedWords:
            FilteredSentence.append(w)
    return FilteredSentence


testSetPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Book.txt"

sample_text = state_unionUTF.raw(testSetPath)

# filteredText = filter_text(sample_text)
# print(filteredText)

