import codecs
from decimal import *

from project.MathSolverRecre.constants import MainPath

tag_list = set()
tag_count = {}
word_set = set()


def get_TrainSet():
    print("In Training\n")
    output_file = MainPath +"project/MathSolverRecre/Preprocessing/Resources/HMM.txt"
    wordtag_list = []

    input_file = codecs.open(MainPath +"project/MathSolverRecre/Preprocessing/Resources/Tagger/Test_Corpus.txt", mode='r', encoding="utf-16")
    lines = input_file.readlines()
    for line in lines:
        line = line.strip('\n')
        data = line.split(" ")
        wordtag_list.append(data)

    input_file.close()
    print("wordtag_list", wordtag_list)
    return wordtag_list


def calculate_Trans_probs():
    print("In Transition Model")
    global tag_list
    global word_set
    train_data = get_TrainSet()
    # print("train data> ",train_data)
    transition_dict = {}
    global tag_count
    for value in train_data:
        # print("Value> ",value)
        previous = "start"
        for data in value:
            # print("value> ", value)
            # print("data> ",data)
            i = data[::-1]
            # print("i> ",i)
            word = data[:-i.find("_") - 1]
            # print("word> ",word)
            fout = codecs.open(MainPath +"project/MathSolverRecre/Preprocessing/Resources/training_wordset.txt", mode='a', encoding="utf-8")
            fout.write(word + "\n")

            word_set.add(word.lower())
            data = data.split("/")
            # print("data",data)
            tag = data[-1]
            # print("tag",tag)
            if (tag.strip() != ''):
                tag_list.add(tag.strip())
            # print("tag list: ",tag_list)

            # counting tags
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1

            # counting bigram tag sequences
            if (previous + "-tag-" + tag) in transition_dict:
                transition_dict[previous.strip() + "-tag-" + tag.strip()] += 1
                previous = tag
            else:
                transition_dict[previous.strip() + "-tag-" + tag.strip()] = 1
                previous = tag
    print("tag_count> ", tag_count)
    print("tag_list> ", tag_list)
    print("word_set> ", word_set)
    print("transition_dict", transition_dict)
    return transition_dict


def set_trans_probs():
    count_dict = calculate_Trans_probs()
    prob_dict = {}
    for key in count_dict:
        den = 0
        val = key.split("-tag-")[0]
        # print("val> ",val)
        for key_2 in count_dict:
            # print("key_2> ",key_2)
            if key_2.split("-tag-")[0] == val:
                den += count_dict[key_2]
        prob_dict[key] = Decimal(count_dict[key]) / (den)
    return prob_dict


def smoothing_probs():
    transition_prob = set_trans_probs()
    for tag in tag_list:
        if "start" + tag not in transition_prob:
            transition_prob[("start" + "-tag-" + tag)] = Decimal(1) / Decimal(len(word_set) + tag_count[tag])
    for tag1 in tag_list:
        for tag2 in tag_list:
            if (tag1 + "-tag-" + tag2) not in transition_prob:
                transition_prob[(tag1 + "-tag-" + tag2)] = Decimal(1) / Decimal(len(word_set) + tag_count[tag1])
    return transition_prob


def calculate_emi_probs():
    # print "In Emission Model"
    train_data = get_TrainSet()
    count_word = {}
    for value in train_data:
        for data in value:
            i = data[::-1]
            # print("i> ",i)
            word = data[:-i.find("/") - 1]
            # print("word> ",word)
            tag = data.split("/")[-1]
            # print("tag> ",tag)
            if word.lower() + "/" + tag in count_word:
                count_word[word.lower() + "/" + tag] += 1
            else:
                count_word[word.lower() + "/" + tag] = 1
    return count_word


def set_emi_probs():
    # print "In Emission Probability"
    global tag_count
    word_count = calculate_emi_probs()
    emission_prob_dict = {}
    for key in word_count:
        emission_prob_dict[key] = Decimal(word_count[key]) / tag_count[key.split("/")[-1]]
    return emission_prob_dict


def generate_training_file():
    global tag_count

    transition_model = smoothing_probs()
    emission_model = set_emi_probs()

    fout = codecs.open(MainPath +"project/MathSolverRecre/Preprocessing/Resources/HMM.txt", mode='w', encoding="utf-8")
    for key, value in transition_model.items():
        # print("key: ", key)
        # print("value: ", value)
        fout.write('%s: %s\n' % (key.strip(), value))

    fout.write(u'Emission Model\n')
    for key, value in emission_model.items():
        # print("key: ",key)
        # print("value: ",value)
        fout.write('%s:%s\n' % (key.strip(), value))

generate_training_file()