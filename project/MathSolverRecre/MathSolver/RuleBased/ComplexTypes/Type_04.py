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


def Type04_solve(tagged, words):
    duplicated = []
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

        # Common_Rule 02 - Get potential variables with attributes( Eg: කුඩාතැපැල්පත්,විශාලතැපැල්පත්)
        if ((tagged[i][1] == "ATT" or tagged[i][1] == "JJ") and (tagged[i + 1][1] == "NNN" or tagged[i][1] == "NNP")):
            word = tagged[i][0] + tagged[i + 1][0]
            tagged[i] = (word, "NNN")
            tagged[i + 1] = tuple("NULL" + "NNN")
            temp = str(words[i + 1])
            # Remove the next NNN after recording it in Required array
            if temp not in required:
                required.append(temp)
            words[i] = word
            words[i + 1] = "NULL"

        # Common_Rule 03 - Remove 'ගුණයක්' when dual multiplication is in the problem
        if ((tagged[i][1] == "CD" or tagged[i][1] == "QFNUM" or tagged[i][1] == "VAR") and (
                tagged[i + 1][0] == "ගුණයක්")):
            tagged[i + 1] = tuple("NULL" + "NNN")
            words[i + 1] = "NULL"

        # Common_Rule 04 - Remove 'ක්' when it occurs after a number or variable
        if ((tagged[i][1] == "CD" or tagged[i][1] == "QFNUM" or tagged[i][1] == "VAR") and (
                tagged[i + 1][0] == "ක්")):
            tagged[i + 1] = tuple("NULL" + "NNN")
            words[i + 1] = "NULL"

        # Common_Rule 05 - Remove NNPI values
        if (tagged[i][1] == "NNPI"):
            NNPI = tagged[i][0]
            temp = ("NULL", "NNN")
            tagged[i] = temp
            words[i] = "NULL"

        # Common_Rule 07 - Remove NNPI values
        if (tagged[i][0] == "මිල" or tagged[i][0] == "ගණන"):
            temp = ("NULL", "NNN")
            tagged[i] = temp
            words[i] = "NULL"

    # Common_Rule 06 - Include identified variables to Required Variables Array
    for i in duplicated:
        required.append(i)

    # Create the final version of Extracted problem

    for i in range(0, len(words)):
        if words[i] in required:
            eddited.append(tagged[i])

        # Common_Rule 07 - Remove NULLs from the sentences
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

            # Template Rule 04 - Replace multiplication
            if (item[i][1] == "MUL"):
                words_inuse[i] = "*"
                item[i] = ("*", "MUL")

            # Template Rule 04 - Tackle "එකතුව" and replace with " Var1 + Var2"
            if ((item[i][0] == "එකතුව" and (item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM"))):
                # Template Rule 05 - Replace "එකතුව" with "+"
                exp = str(variablesReplace[0][1] + " + " + variablesReplace[1][1])
                words_inuse[i] = exp
                temp = (exp, "EXP")
                item[i] = temp
                # Put Equivalance to expression
                words_inuse.insert(i + 1, "=")
                temp = ("=", "EQ")
                item.insert(i + 1, temp)

            # Template Rule 05 - Replace Addition with "හා" and "සහ"
            if (item[i][1] == "ADD" or item[i][0] == "හා" or item[i][0] == "සහ" or item[i][0] == "වඩා"):
                words_inuse[i] = "+"
                temp = ("+", "ADD")
                item[i] = temp

            # Template Rule 06- Apply multiplication and generate Variable
            if ((item[i][1] == "VAR") and (item[i + 1][1] == "MUL") and (
                    item[i + 2][1] == "CD" or item[i + 2][1] == "QFNUM" or item[i + 2][1] == "VAR")):
                multiplied = str(item[i + 2][0]) + str(item[i][0])
                temp = (multiplied, "VAR")
                words_inuse[i] = multiplied
                words_inuse[i + 1] = words_inuse[i + 2] = "="
                item[i] = temp
                item[i + 1] = item[i + 2] = ("NULL", "NULL")

                # Template Rule 06- Apply multiplication and generate Variable
                if ((item[i][1] == "VAR") and (item[i + 1][1] == "MUL") and (
                        item[i + 2][1] == "CD" or item[i + 2][1] == "QFNUM" or item[i + 2][1] == "VAR")):
                    multiplied = str(item[i + 2][0]) + str(item[i][0])
                    temp = (multiplied, "VAR")
                    words_inuse[i] = multiplied
                    words_inuse[i + 1] = words_inuse[i + 2] = "="
                    item[i] = temp
                    item[i + 1] = item[i + 2] = ("NULL", "NULL")

            # Template Rule 06- Apply multiplication and generate Variable
            if ((item[i][1] == "VAR") and (
                    item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM" or item[i + 1][1] == "VAR") and (
                    item[i + 2][1] == "MUL")):
                multiplied = str(item[i + 1][0]) + str(item[i][0])
                temp = (multiplied, "VAR")
                words_inuse[i] = multiplied
                words_inuse[i + 1] = words_inuse[i + 2] = "="
                item[i] = temp
                item[i + 1] = item[i + 2] = ("NULL", "NULL")

            # Template Rule 07 - Replace multiplication by "බැගින්"
            if ((item[i][1] == "CD" or item[i][1] == "QFNUM") and (item[i + 1][0] == "බැගින්")):
                words_inuse[i + 1] = "*"
                temp = ("*", "MUL")
                item[i + 1] = temp
                # Swapping
                swap = item[i]
                item[i] = item[i + 1]
                item[i + 1] = swap
                swap2 = words_inuse[i]
                words_inuse[i] = words_inuse[i + 1]
                words_inuse[i + 1] = swap2

            # Template Rule 08 - Tackle "එකතුව" and replace with " Var1 + Var2"
            if ((item[i][0] == "එකතුව" and (item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM"))):
                # Template Rule 05 - Replace "එකතුව" with "+"
                exp = str(variablesReplace[0][1] + " + " + variablesReplace[1][1])
                words_inuse[i] = exp
                temp = (exp, "EXP")
                item[i] = temp
                # Put Equivalance to expression
                words_inuse.insert(i + 1, "=")
                temp = ("=", "EQ")
                item.insert(i + 1, temp)

            #  Template Rule 07 - Identifying Equivalance method.
            if ((item[i][1] == "VAR") and (item[i - 1][1] == "ADD") and (item[i - 2][1] == "VAR") and (
                    item[i + 1][1] == "CD" or item[i + 1][1] == "QFNUM")):
                temp = ("=", "EQ")
                item.insert(i + 1, temp)
                words_inuse.insert(i + 1, "=")

            print(item)
            #  Template Rule 07 - Identifying Equivalance method.
            if ((item[i][1] == "VAR") and (item[i + 1][0] == "වඩා") and (item[i + 2][1] == "NNN") and (
                    item[i + 3][1] == "CD") and (item[i + 4][1] != "VP" or item[i + 4][1] != "VJJ")):
                temp1 = item[i + 1]
                temp2 = words_inuse[i + 1]
                item[i + 1] = item[i + 2]
                words_inuse[i + 1] = words_inuse[i + 2]
                item[i + 2] = temp1
                words_inuse[i + 2] = temp2
                # words_inuse.insert(i, "=")
                # temp = ("=", "EQ")
                # item.insert(i, temp)

            # Template Rule 08 - Identifying Equivalance method with "නම්" word
            if (item[i][0] == "නම්"):
                temp = ("=", "EQ")
                item[i] = temp
                words_inuse[i] = "="

            #  Template Rule 09 - Identifying Equivalance method with "ඇත" after a variable
            if ((item[i][1] == "VAR" or item[i][1] == "QFNUM" or item[i][1] == "CD") and (item[i + 1][0] == "ඇත")):
                temp = ("=", "EQ")
                item.insert(i, temp)
                words_inuse.insert(i, "=")
                # temp2 = ("NULL", "NULL")
                # item[i] = temp2
                # words_inuse[i] = "NULL"

    # Build Expressions
    for item in splittedEdit:
        # print(item)
        dup = []
        finalPart = []
        varCheckArray = []
        checkArray = []
        for i in range(0, len(item)):
            # Get only required things to build Expression
            if (item[i][1] == "ADD" or item[i][1] == "VAR" or item[i][1] == "SUB" or item[i][1] == "EQ" or item[i][
                1] == "MUL" or item[i][1] == "CD" or item[i][1] == "QFNUM" or item[i][1] == "EXP"):
                finalPart.append(item[i][0])

            if (item[i][1] == "VAR"):
                varCheckArray.append(item[i][0])
            if (item[i][1] == "VAR" or item[i][1] == "CD" or item[i][1] == "QFNUM"):
                checkArray.append(item[i][0])

        for i in finalPart:
            #  Template Rule 18 - Check Duplications
            if i in varCheckArray:
                if i in dup:
                    dup.append(i)

        for i in range(0, len(finalPart)):

            #  Template Rule 18 - Remove Unnecessary "*" chars
            if (finalPart[i] == "*" and (i + 1 < len(finalPart) and finalPart[i + 1] == "+")):
                del finalPart[i]
                finalPart.insert(len(finalPart), "NULL")

            # Template Rule 15 - Swap variables to get correct format of the equation

            if ((finalPart[i] in varCheckArray) and (
                    i + 1 < len(finalPart) and finalPart[i + 1] in varCheckArray) and len(dup) == 0):
                k = i + 1
                finalPart.insert(k, "=")

            #  Template Rule 18 - Remove double "=" chars
            if (finalPart[i] == "=" and (i + 1 < len(finalPart) and finalPart[i + 1] == "=")):
                finalPart[i] = "NULL"

            # Template Rule 18 - Remove Unnecessary "+" chars
            if ((finalPart[i] == "+") and (i + 1 < len(finalPart) and finalPart[i + 1] in checkArray) and (
                    i + 2 < len(finalPart) and finalPart[i + 2] == "+")):
                finalPart[i + 2] = "NULL"

        #  Template Rule 17 - Filter NULL s from expression
        finalPart = list(filter(lambda x: x != "NULL", finalPart))

        if finalPart not in finalExp:
            finalExp.append(finalPart)

    print("----------------------------------------------------------------------------------------")
    print(variablesReplace)
    print(finalExp)
    print(NNPI)
    return variablesReplace, finalExp, NNPI
