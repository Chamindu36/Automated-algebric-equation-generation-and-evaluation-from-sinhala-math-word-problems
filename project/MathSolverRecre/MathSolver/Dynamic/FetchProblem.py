
import nltk

from project.MathSolverRecre.Preprocessing.Tagger.TaggerUse import sentence_tag_in_array_style
from project.MathSolverRecre.Preprocessing.Utils.PrepareData import prepare_data
from project.MathSolverRecre.Preprocessing.Utils.Tokenizer import tokenize_texts

nltk.download('perluniprops')

def fetch_problem(s):
    print("processing: " + s)
    nums = []
    vars = []
    subs = []
    mapped = list
    # Tokenize the words from given sentence
    words = tokenize_texts(s)
    numcounter = 1
    varcounter = 0
    subcounter = 0

    # POS tagging sentence
    tagged = sentence_tag_in_array_style(s)

    # Process tagged data
    words, numcounter, nums,tagged  = prepare_data(words, numcounter, nums, tagged,False)

    for i in range(0, len(words)):
        if (tagged[i][1] == "NNN" or tagged[i][1] == "ATT"):
            if(words[i] not in subs):
                subs.append(words[i])
                subcounter +=1
            words[i] = words[i] + "(S" + str(subcounter) + ")"


        if (tagged[i][1] == "VAR"):
            if(words[i] not in vars):
                vars.append(words[i])
                varcounter += 1
            words[i] = words[i] + "(V" + str(varcounter) + ")"

    # print("Results for model -----------------------------------------------------------------------------------------")
    # print(words)
    # print(nums)
    # print(vars)
    # print(subs)
    print(tagged)
    print(words)
    return words,nums,vars,subs


sent = "නයනිට ඇයගේ කැටය කැඩීමෙන් රුපියල් 5000 ක මුදලක් ලබා ගත්තාය. එහි කාසි වලින් තිබු මුදල මෙන් 4 ගුණයක් නෝට්ටු වලින් තිබුණි. කාසි වලින් හා නෝට්ටු වලින් ලැබුණු ගණන වෙන වෙනම සොයන්න"
# fetch_problem(sent)
