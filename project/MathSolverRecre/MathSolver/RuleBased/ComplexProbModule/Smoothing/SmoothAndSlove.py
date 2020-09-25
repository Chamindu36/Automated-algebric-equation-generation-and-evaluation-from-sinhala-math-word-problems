import re




# Smoothing for type 01
from project.MathSolverRecre.MathSolver.RuleBased.ComplexProbModule.SimultaneousEqSolve import solve_Simultaneous_Equations


def Smooth_Type_01(variablesReplace, finalExp, NNPI):
    inputArray = finalExp
    outPutExp = []
    output = []
    varArray = variablesReplace
    checkMULU = str(varArray)
    k = ''
    os = []
    context = False
    # Check "මුලු" and "මුළු" keywords and make
    if (("මුලු" in checkMULU) or ("මුළු" in checkMULU)):
        for i in varArray:
            item = str(i[0])
            item = item.strip()
            if (("මුලු" in item) or ("මුළු" in item)):
                k = i
            else:
                os.append(i[1])
        for i in varArray:
            if (i == k):
                exp = os[0] + "+" + os[1] + "=" + k[1]
                exp.strip()
                inputArray.append(exp)

    for i in range(len(inputArray)):
        # for j in range(len(arr[i])):
        eq = inputArray[i]
        listToStr = ''.join(map(str, eq))

        k = listToStr.strip()
        # print(k)
        x = re.compile(r'(([0-9]*)?)([a-z])?\s*\+?-?\s*?(([0-9]*)?)([a-z])?\s*?=\s*(([0-9])+)?([a-z])?')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            outPutExp.append(p)
            # print(p)

    for i in range(len(outPutExp)):
        k = outPutExp[i]
        k = k.strip()
        x = re.compile(r'(\d*[a-z]\s*\=(\s*)\d*[a-z])')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            p = str(p)
            p = p.strip()
            items = p.split("=")
            exp = str(items[0] + "-" + items[1] + ' = 0' )
            outPutExp[i] = exp

    for i in range (0,len(varArray)):
        k = str(varArray[i][0])
        j = i + 1
        for j in range(len(varArray)):
            l = str(varArray[j][0])
            if (k in l):
                context = True

    # if (context is True):
    #     exp = str(varArray[0][1] + '=' + varArray[1][1] + '+' + varArray[2][1])
    #     print(exp)
    #     outPutExp.append(exp)

    print(varArray)
    print(outPutExp)
    print(NNPI)
    answers = solve_Simultaneous_Equations(outPutExp)
    # print(answers)
    return varArray, outPutExp, NNPI, answers


# Smoothing for type 02
def Smooth_Type_02(variablesReplace, finalExp, NNPI):
    inputArray = finalExp
    outPutExp = []

    varArray = variablesReplace
    checkMULU = str(varArray)
    k = ''
    os = []
    ot = ''
    # Check "මුලු" and "මුළු" keywords and make
    if (("මුලු" in checkMULU) or ("මුළු" in checkMULU)):
        for i in varArray:
            item = str(i[0])
            item = item.strip()
            if (("මුලු" in item) or ("මුළු" in item)):
                k = i
            else:
                os.append(i[1])

        for i in varArray:
            if (i == k):
                exp = os[0] + "+" + os[1] + "=" + k[1]
                exp.strip()
                inputArray.append(exp)

    for i in range(len(inputArray)):
        # for j in range(len(arr[i])):
        eq = inputArray[i]
        listToStr = ' '.join(map(str, eq))

        k = listToStr.strip()
        x = re.compile(r'(([0-9]*)?)([a-z])\s\+?\s?(([0-9])+)?([a-z])?\s?\=\s(([0-9])+)?([a-z])?')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            outPutExp.append(p)
            # print(p)

    print(varArray)
    print(outPutExp)
    print(NNPI)
    answers = solve_Simultaneous_Equations(outPutExp)
    return varArray, outPutExp, NNPI, answers


# Smoothing for type 03
def Smooth_Type_03(variablesReplace, finalExp, NNPI):
    inputArray = finalExp
    outPutExp = []

    varArray = variablesReplace
    checkMULU = str(varArray)
    k = ''
    os = []
    ot = ''
    context = False
    # Check "මුලු" and "මුළු" keywords and make
    if (("මුලු" in checkMULU) or ("මුළු" in checkMULU)):
        for i in varArray:
            item = str(i[0])
            item = item.strip()
            if (("මුලු" in item) or ("මුළු" in item)):
                k = i
            else:
                os.append(i[1])

        for i in varArray:
            if (i == k):
                exp = os[0] + "+" + os[1] + "=" + k[1]
                exp.strip()
                inputArray.append(exp)

    for i in range(len(inputArray)):
        # for j in range(len(arr[i])):
        eq = inputArray[i]
        listToStr = ''.join(map(str, eq))

        k = listToStr.strip()
        x = re.compile(r'((\d*[a-z]\s*[\+|-]\s*\d*[a-z]\s*\=\s*\d*)|(\d*[a-z]\s*\=\s*\d*[a-z]\s*[\+|-]\s*\d+))')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            outPutExp.append(p)
            # print(p)

    for i in range(len(outPutExp)):
        k = outPutExp[i]
        k = k.strip()
        x = re.compile(r'(\d*[a-z]\s*[\+|-]\s*\d*\s*\=\s*\d*[a-z])')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            p = str(p)
            p = p.strip()
            items = p.split("=")
            if('+' in items[0]):
                gus = items[0].split("+")
                exp = str(gus[0] + "-" + items[1] + ' = '+str('-'+gus[1]))
            elif ('-' in items[0]):
                exp = str(gus[0] + "-" + items[1] + ' = '+gus[1])
            # print(exp)
            outPutExp[i] = exp

    for i in range(len(outPutExp)):
        k = outPutExp[i]
        k = k.strip()
        x = re.compile(r'(\d*[a-z]\s*\=\s*\d*[a-z]\s*[\+|-]\s*\d+)')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            p = str(p)
            p = p.strip()
            items = p.split("=")
            if('+' in items[1]):
                gus = items[1].split("+")
                exp = str(items[0] + "-" + gus[0] + ' = '+gus[1])
            elif ('-' in items[1]):
                exp = str(items[0] + "-" + gus[0] + ' = ' + gus[1])
            # print(exp)
            outPutExp[i] = exp

    if(len(varArray)>2):
        for i in range (0,len(varArray)):
            k = str(varArray[i][0])
            j = i + 1
            for j in range(len(j,varArray)):
                l = str(varArray[j][0])
                if (k in l):
                    # print(k,l)
                    context = True

    if (context is True):
        exp = str(varArray[0][1] + '=' + varArray[1][1] + '+' + varArray[2][1])
        # print(exp)
        outPutExp.append(exp)

    print(varArray)
    print(outPutExp)
    print(NNPI)
    answers = solve_Simultaneous_Equations(outPutExp)
    return varArray, outPutExp, NNPI, answers


# Smoothing for type 04
def Smooth_Type_04(variablesReplace, finalExp, NNPI):
    inputArray = finalExp
    outPutExp = []

    varArray = variablesReplace
    checkMULU = str(varArray)
    k = ''
    os = []
    ot = ''
    context = False
    # Check "මුලු" and "මුළු" keywords and make
    if (("මුලු" in checkMULU) or ("මුළු" in checkMULU)):
        for i in varArray:
            item = str(i[0])
            item = item.strip()
            if (("මුලු" in item) or ("මුළු" in item)):
                k = i
            else:
                os.append(i[1])

        for i in varArray:
            if (i == k):
                exp = os[0] + "+" + os[1] + "=" + k[1]
                exp.strip()
                inputArray.append(exp)

    for i in range(len(inputArray)):
        # for j in range(len(arr[i])):
        eq = inputArray[i]
        listToStr = ''.join(map(str, eq))

        k = listToStr.strip()
        x = re.compile(r'((\d*[a-z]\s*[\+|-]\s*\d*\s*\=\s*\d*[a-z])|(\d*[a-z]\s*[\+|-]\s*\d*[a-z]\s*\=\s*\d+)|(\d*[a-z]\s*\=\d*[a-z]\s*[\+|-]\d+))')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            outPutExp.append(p)
            # print(p)

    for i in range(len(outPutExp)):
        k = outPutExp[i]
        k = k.strip()
        x = re.compile(r'(\d*[a-z]\s*[\+|-]\s*\d*\s*\=\s*\d*[a-z])')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            p = str(p)
            p = p.strip()
            items = p.split("=")
            if('+' in items[0]):
                gus = items[0].split("+")
                exp = str(gus[0] + "-" + items[1] + ' = '+str('-'+gus[1]))
            elif ('-' in items[0]):
                exp = str(gus[0] + "-" + items[1] + ' = '+gus[1])
            # print(exp)
            outPutExp[i] = exp

    for i in range(len(outPutExp)):
        k = outPutExp[i]
        k = k.strip()
        x = re.compile(r'(\d*[a-z]\s*\=\s*\d*[a-z]\s*[\+|-]\s*\d+)')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            p = str(p)
            p = p.strip()
            items = p.split("=")
            if('+' in items[1]):
                gus = items[1].split("+")
                exp = str(items[0] + "-" + gus[0] + ' = '+gus[1])
            elif ('-' in items[1]):
                exp = str(items[0] + "-" + gus[0] + ' = ' + gus[1])
            # print(exp)
            outPutExp[i] = exp

    if(len(varArray)>2):
        for i in range (0,len(varArray)-1):
            k = str(varArray[i][0])
            j = i + 1
            for j in range(len(varArray)):
                l = str(varArray[j][0])
                if (k in l):
                    # print(k,l)
                    context = True

    if (context is True):
        exp = str(varArray[0][1] + '=' + varArray[1][1] + '+' + varArray[2][1])
        # print(exp)
        outPutExp.append(exp)

    print(varArray)
    print(outPutExp)
    print(NNPI)
    answers = solve_Simultaneous_Equations(outPutExp)
    return varArray, outPutExp, NNPI, answers


# Smoothing for type 05
def Smooth_Type_05(variablesReplace, finalExp, NNPI):
    inputArray = finalExp
    outPutExp = []

    varArray = variablesReplace
    checkMULU = str(varArray)
    k = ''
    os = []
    ot = ''
    # Check "මුලු" and "මුළු" keywords and make
    if (("මුලු" in checkMULU) or ("මුළු" in checkMULU)):
        for i in varArray:
            item = str(i[0])
            item = item.strip()
            if (("මුලු" in item) or ("මුළු" in item)):
                k = i
            else:
                os.append(i[1])

        for i in varArray:
            if (i == k):
                exp = os[0] + "+" + os[1] + "=" + k[1]
                exp.strip()
                inputArray.append(exp)

    for i in range(len(inputArray)):
        # for j in range(len(arr[i])):
        eq = inputArray[i]
        listToStr = ' '.join(map(str, eq))

        k = listToStr.strip()
        x = re.compile(r'(([0-9])+)?(([a-z]))?\s\+?-?\s(([0-9])+)?\s?([a-z])?\s?\=\s?([a-z])?\s?(([0-9])+)?')
        n = x.search(k)
        if (n is None):
            continue
        else:
            p = n.group(0)
            outPutExp.append(p)
            # print(p)

    print(varArray)
    print(outPutExp)
    print(NNPI)
    answers = solve_Simultaneous_Equations(outPutExp)
    return varArray, outPutExp, NNPI, answers
