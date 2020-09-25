import collections


# Method to split a list by given values
def split_list_by_Val(givenList, value):
    size = len(givenList)
    idx_list = [idx + 1 for idx, val in
                enumerate(givenList) if val == value]

    res = [givenList[i: j] for i, j in
           zip([0] + idx_list, idx_list +
               ([size] if idx_list[-1] != size else []))]
    return res


def Type05_solve(tagged, words):
    global duplicated
    subs = []
    required = []
    eddited = []
    NNPI = "ගණන"
    print(tagged)
    for i in range(0, len(words)):

        # Common_Rule 01 - Get all the potential variables from the problem
        if (tagged[i][1] == "NNP" or tagged[i][1] == "ATT" or tagged[i][1] == "NNN"):
            subs.append(words[i])
            duplicated = ([item for item, count in collections.Counter(subs).items() if count > 1])

            # Common_Rule 02 - Remove NNPI values
            if (tagged[i][0] == "මිල" or tagged[i][0] == "ගණන"):
                temp = ("NULL", "NNN")
                tagged[i] = temp
                words[i] = "NULL"

        # # Common_Rule 03 - Get noun and "මිල" as a single noun( Eg: මේසයේමිල,බංකුවේමිල)
        # if ((tagged[i][1] == "NNN" or tagged[i][1] == "PRP") and (tagged[i + 1][0] == "මිල")):
        #     word = tagged[i][0] + tagged[i + 1][0]
        #     tagged[i] = (word, "NNN")
        #     tagged[i + 1] = tuple("NULL" + "NNN")
        #     temp = str(words[i + 1])
        #     # Remove the next NNN after recording it in Required array
        #     if temp not in required:
        #         required.append(temp)
        #     words[i] = word
        #     words[i + 1] = "NULL"

        # Common_Rule 05 - Add "," after word "අතර"
        if (tagged[i][0] == "අතර"):
            words.insert(i + 1, ",")
            temp = (",", ".")
            tagged.insert(i + 1, temp)

        # Common_Rule 06 - Add "," and replace with "."
        if (tagged[i][0] == ","):
            words.insert(i + 1, ".")
            temp = (".", ".")
            tagged.insert(i + 1, temp)

        # Common_Rule 07 - Remove 'ගුණයක්' when dual multiplication is in the problem
        if ((tagged[i][1] == "CD" or tagged[i][1] == "QFNUM" or tagged[i][1] == "VAR") and (
                tagged[i + 1][0] == "ගුණයක්")):
            tagged[i + 1] = tuple("NULL" + "NNN")
            words[i + 1] = "NULL"

        # Common_Rule 08 - Remove 'ක්' when it occurs after a number or variable
        if ((tagged[i][1] == "CD" or tagged[i][1] == "QFNUM" or tagged[i][1] == "VAR") and (
                tagged[i + 1][0] == "ක්")):
            tagged[i + 1] = tuple("NULL" + "NNN")
            words[i + 1] = "NULL"

        # Common_Rule 09 - Remove NNPI values
        if (tagged[i][1] == "NNPI"):
            NNPI = tagged[i][0]
            temp = ("NULL", "NNN")
            tagged[i] = temp
            words[i] = "NULL"

        # Common_Rule 10 - Include identified variables to Required Variables Array
    for i in duplicated:
        required.append(i)

        # Create the final version of Extracted problem
    for i in range(0, len(words)):
        if words[i] in required:
            eddited.append(tagged[i])

        # Common_Rule 11 - Remove NULLs from the sentences
        if words[i] == "NULL":
            continue

        elif (words[i] not in subs):
            eddited.append(tagged[i])

    splittedEdit = split_list_by_Val(eddited, ('.', '.'))
    print(splittedEdit)

    variCounter = 0
    varPuts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'i', 'j', 'k', 'l', 'm']
    variablesReplace = []
    variables = []
    finalExp = []
    for item in splittedEdit:
        words_inuse = []
        for i in range(0, len(item)):
            words_inuse.append(item[i][0])

        for i in range(0, len(item)):
            print(item)

            # Template Rule 01 - Map variables with expressions
            if (item[i][1] == "NNP" or item[i][1] == "ATT" or item[i][1] == "NNN"):
                # Check for Duplication
                if (words_inuse[i] not in variables):
                    variables.append(words_inuse[i])
                    temp = (words_inuse[i], varPuts[variCounter])
                    variablesReplace.append(temp)
                    variCounter += 1
                # Template Rule 02- Replace with mapped letters
                if (words_inuse[i] in variables):

                    # Template Rule 03 = Exclude 'ගණන' from being a variable
                    if (words_inuse[i] != 'ගණන'):
                        reqVar = ''
                        for k in range(0, len(variablesReplace)):
                            if (words_inuse[i] == variablesReplace[k][0]):
                                reqVar = str(variablesReplace[k][1])
                        words_inuse[i] = reqVar
                        temp = (words_inuse[i], "VAR")
                        item[i] = temp

            # Template Rule 01 - Tackle "එකතුව" and replace with " Var1 + Var2"
            if ((item[i][0] == "එකතුව" and (item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM"))):
                # Template Rule 05 - Replace "එකතුව" with "+"
                exp = str("a " + " + " + " b")
                words_inuse[i] = exp
                temp = (exp, "EXP")
                item[i] = temp
                # Put Equivalance to expression
                words_inuse.insert(i + 1, "=")
                temp = ("=", "EQ")
                item.insert(i + 1, temp)

            # Template Rule 02 - Find the word "මුළු" and get that the meaning is "x + y"
            if (item[i][0] == "මුළු" or item[i][0] == "මුලු" or item[i][0] == "එකතුව"):
                k = i
                # Generate the Expression
                while (item[k][1] != "."):
                    if (item[k][1] == "CD" or item[k][1] == "QFNUM"):
                        stringGen = str("a + b = " + item[k][0])
                        exp = (stringGen, "EXP")
                        item[i + 1] = exp
                        break
                    else:
                        k += 1

            # Template Rule 03 - Find the word "වෙනස" and get that the meaning is "x - y"
            if (item[i][0] == "වෙනස"):
                k = i
                # Generate the Expression
                while (item[k][1] != "."):
                    if (item[k][1] == "CD" or item[k][1] == "QFNUM"):
                        stringGen = str("a - b = " + item[k][0])
                        exp = (stringGen, "EXP")
                        item[i + 1] = exp
                        break
                    else:
                        k += 1

            # Template Rule 04 - Replace Addition with "හා" and "සහ"
            if (item[i][1] == "ADD" or item[i][0] == "හා" or item[i][0] == "සහ"):
                words_inuse[i] = "+"
                temp = ("+", "ADD")
                item[i] = temp

            #  Template Rule 05 - Identifying Equivalance method.
            if ((item[i][1] == "VAR") and (
                    item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM" or item[i + 1][1] == "VAR")):
                words_inuse.insert(i + 1, "=")
                temp = ("=", "EQ")
                item.insert(i + 1, temp)

            #  Template Rule 06 - Identifying Equivalance method with "නම්" word
            if (item[i][0] == "නම්"):
                temp = ("=", "EQ")
                item[i] = temp
                words_inuse[i] = "="

            #  Template Rule 07 - Identifying Equivalance method with "සඳහා" word
            if (item[i][0] == "සඳහා"):
                temp = ("=", "EQ")
                item[i] = temp
                words_inuse[i] = "="

    # Build Expressions
    for item in splittedEdit:
        # print(item)
        finalPart = []
        for i in range(0, len(item)):
            # Get only required things to build Expression
            if (item[i][1] == "EXP"):
                finalPart.append(item[i][0])
        if finalPart not in finalExp:
            finalExp.append(finalPart)

    print("----------------------------------------------------------------------------------------")
    print(finalExp)
    print(NNPI)
    variablesReplace = []
    return variablesReplace, finalExp, NNPI
