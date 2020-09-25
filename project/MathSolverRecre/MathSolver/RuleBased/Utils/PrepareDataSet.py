import operator
import pdb

from nltk.tokenize.moses import MosesDetokenizer
import nltk
nltk.download('perluniprops')

from project.MathSolverRecre.Preprocessing.Tagger.TaggerUse import sentence_tag_in_array_style
from project.MathSolverRecre.Preprocessing.Utils.PrepareData import prepare_data
from project.MathSolverRecre.Preprocessing.Utils.Tokenizer import tokenize_texts


def preprocess_sinhala(s):
    nums = []
    # Tokenize the words from given sentence
    words = tokenize_texts(s)
    numcounter = 1
    # POS tagging sentence
    tagged = sentence_tag_in_array_style(s)

    # Process tagged data
    words, numcounter, nums ,tagged = prepare_data(words, numcounter, nums, tagged, True)
    print(words)
    output = [words, numcounter, nums]
    return output


def build_phrases(strings, nWords, minRepeats):
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


def initialize_WordsList(strings):
    # for arithmetic, 9,5,5,4,3
    wdlst = (build_phrases(strings, 1, 20) + build_phrases(strings, 2, 10) + build_phrases(strings, 3,
                                                                                           9) + build_phrases(
        strings, 4, 8) + build_phrases(strings, 5, 7))
    print("wordlist: ", wdlst)
    return wdlst


def make_map(strs, wordslist):
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

