from decimal import Decimal
from fractions import Fraction

from project.MathSolverRecre.Preprocessing.Utils.ProcessSInhalaValues import sinhala_Value_process


def prepare_data(words, numcounter, nums, tagged, forANN):
    for i in range(0, len(words)):
        if (i < len(words) and (words[i] == "මහතා" or words[i] == "මහත්මිය" or words[i] == "වහන්සේ")):
            del words[i]
            del tagged[i]

    # # processing parantehtical numbers eg: twenty-two (22)
    # for i in range(0, len(words)):  # for each word in the string
    #     if (i < len(words) and words[i][0] == "("):  # if the word is a parantehtical
    #         nums.append(int(words[i + 1]))  # add whats inside the parentheses (a number) to the numbers
    #         del words[i + 2]
    #         del words[i]  # delete the instance of the paranthetical
    #         del words[i - 1]
    #         words[i - 1] = "N" + str(
    #             numcounter)  # replace the word before the parenthetical (the written-out number) with the numbertext
    #         numcounter += 1

    # processing fractions eg: 3/2
    for i in range(0, len(words)):
        if (i < len(words) and "/" in words[i]):
            if (words[i - 1][0].isdigit()):
                nums.append(Fraction(int(words[i - 1]) * int(words[i].split("/")[1]) + int(words[i].split("/")[0]),
                                     int(words[i].split("/")[1])))
                del words[i]
                del tagged[i]
                words[i - 1] = "N" + str(numcounter)
                temp = ("N" + str(numcounter), "CD")
                tagged[i - 1] = temp
            else:
                nums.append(Fraction(int(words[i].split("/")[0]), int(words[i].split("/")[1])))
                words[i] = "N" + str(numcounter)
                temp = ("N" + str(numcounter), "CD")
                tagged[i] = temp
            numcounter += 1
    # Proceeing most frequent sinhla values
    words, numcounter, nums ,tagged = sinhala_Value_process(words, numcounter, nums,tagged)

    # processing normal numbers eg: 253, 12.2
    if forANN == True:
        for i in range(0, len(words)):
            # print(words[i])
            # if (words[i][len(words[i])-1].isalnum()==False):
            #     words[i] = words[i][:-1]
            if (words[i][0].isdigit() and words[i][len(words[i]) - 1].isdigit()):
                # print(words[i])
                nums.append(Decimal(words[i].replace(',', '')))
                words[i] = "N" + str(numcounter)
                temp = ("N" + str(numcounter), "CD")
                tagged[i] = temp
                numcounter += 1



    return words, numcounter, nums, tagged
