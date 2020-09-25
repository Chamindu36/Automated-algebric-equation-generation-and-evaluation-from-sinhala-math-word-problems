import codecs
from decimal import *

from pip._vendor.msgpack.fallback import xrange

tag_set = set()
word_set = set()


def get_train_data():
    inputFile = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/HMM.txt"
    output_file = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/ViterbiOutput.txt"
    transition_prob = {}
    emission_prob = {}
    tag_list = []
    tag_count = {}
    global tag_set

    input_file = codecs.open(inputFile, mode='r', encoding="utf-8")
    lines = input_file.readlines()
    flag = False
    for line in lines:
        line = line.strip('\n')
        if line != "Emission Model":
            i = line[::-1]
            key_insert = line[:-i.find(":") - 1]
            # print("key_insert",key_insert)
            value_insert = line.split(":")[-1]
            # print("value_insert", value_insert)
            if flag == False:
                transition_prob[key_insert] = value_insert  # getting transition probabilities
                if (key_insert.split("-tag-")[0] not in tag_list) and (key_insert.split("-tag-")[0] != "start"):
                    tag_list.append(key_insert.split("-tag-")[0])
            else:
                emission_prob[key_insert] = value_insert  # getting emission probabilities
                key_tag = line[:-i.find(":") - 1]
                val = key_tag.split("/")[-1]  # getting the tag
                j = key_insert[::-1]
                word = key_insert[:-j.find("/") - 1]  # getting the word
                # print("word> ",word)
                word_set.add(word.lower())
                if val in tag_count:
                    tag_count[val] += 1  # counting an existing tag
                else:
                    tag_count[val] = 1  # counting a new tag
                tag_set.add(val)

        else:
            flag = True
            continue

    input_file.close()

    return tag_list, transition_prob, emission_prob, tag_count, word_set


def viterbi_process(sentence, tags, transition_prob, emission_prob, tag_count, word_set):
    global tag_set
    sentence = sentence.strip("\n")
    word_list = sentence.split(" ")


    current_prob = {}
    for tag in tags:
        tp = Decimal(0)
        em = Decimal(0)
        if "start-tag-" + tag in transition_prob:  # calculating probabilities for start tag/word
            tp = Decimal(transition_prob["start-tag-" + tag])
        if word_list[0].lower() in word_set:
            if (word_list[0].lower() + "/" + tag) in emission_prob:
                em = Decimal(emission_prob[word_list[0].lower() + "/" + tag])
                current_prob[tag] = tp * em
        else:
            em = Decimal(1) / (tag_count[tag] + len(word_set))  # for an unknown word
            current_prob[tag] = tp

    if len(word_list) == 1:
        max_path = max(current_prob, key=current_prob.get)
        return max_path
    else:

        for i in xrange(1, len(word_list)):
            previous_prob = current_prob
            # print("i> ",i)
            # print("previous_prob",previous_prob)
            current_prob = {}
            locals()['dict{}'.format(i)] = {}
            previous_tag = ""
            for tag in tags:
                # print(word_list)
                if word_list[i].lower() in word_set:
                    # print("word> ",word_list[i].lower())
                    if word_list[i].lower() + "/" + tag in emission_prob:
                        # print("has emission")
                        em = Decimal(emission_prob[word_list[i].lower() + "/" + tag])
                        max_prob, previous_state = max((Decimal(previous_prob[previous_tag]) * Decimal(transition_prob[previous_tag + "-tag-" + tag]) * em, previous_tag) for previous_tag in previous_prob)
                        current_prob[tag] = max_prob
                        locals()['dict{}'.format(i)][previous_state + "-" + tag] = max_prob
                        previous_tag = previous_state
                        # print("previous_tag",previous_tag)
                else:  # for unknown words
                    em = Decimal(1) / (tag_count[tag] + len(word_set))
                    # print("jdkdjkhk",tag)
                    max_prob, previous_state = max((Decimal(previous_prob[previous_tag]) * Decimal(transition_prob[previous_tag + "-tag-" + tag]) * em, previous_tag) for previous_tag in previous_prob)
                    current_prob[tag] = max_prob
                    locals()['dict{}'.format(i)][previous_state + "-" + tag] = max_prob
                    previous_tag = previous_state
            if i == len(word_list) - 1:
                max_path = ""
                last_tag = max(current_prob, key=current_prob.get)
                max_path = max_path + last_tag + " " + previous_tag
                for j in range(len(word_list) - 1, 0, -1):
                    for key in locals()['dict{}'.format(j)]:
                        data = key.split("-")
                        if data[-1] == previous_tag:
                            max_path = max_path + " " + data[0]
                            previous_tag = data[0]
                            break
                result = max_path.split()
                result.reverse()
                return " ".join(result)

def HMM_tagging():
    tag_list, transition_model, emission_model, tag_count, word_set = get_train_data()
    input_file = codecs.open("D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Book.txt", mode='r', encoding="utf-8")
    fout = codecs.open("D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/ViterbiOutput.txt", mode='w', encoding="utf-8")
    for sentence in input_file.readlines():
        # print("New Sentence\n")
        path = viterbi_process(sentence.strip(), tag_list, transition_model, emission_model, tag_count, word_set)
        # print("path> ",path)
        sentence = sentence.rstrip('\r\n')
        # print("sentence> ",sentence)
        word = sentence.strip().split(" ")
        # print("word> ",word)
        tag = path.split(" ")
        sentence=[]
        # print("tag> ",tag)
        for j in range(0, len(word)):
            if j == len(word) - 1:
                # print("OO> ",word[j])
                temp = word[j] + "/" + tag[j] + u'\n'
                fout.write(temp)
                sentence.append(temp)
            else:
                temp=word[j] + "/" + tag[j] + " "
                fout.write(temp)
                sentence.append(temp)
        print(sentence)

HMM_tagging()
