import re

import numpy as np


def solve_Simultaneous_Equations(equations):
    try:
        EqList = equations
        eq1 = EqList[0]
        eq2 = EqList[1]

        contentEq1 = eq1.split("=")
        result1 = contentEq1[1].strip()
        result1= re.sub(r"\s+", "", result1)
        result1 = int(result1)
        contentEq2 = eq2.split("=")
        result2 = contentEq2[1].strip()
        result2= re.sub(r"\s+", "", result2)
        result2 = int(result2)
        # print(result2)
        e1 = contentEq1[0]
        str(e1)
        if ('+' in e1):
            items = e1.split('+')
            # print(items)
            f1 = items[0].strip()
            f2 = items[1].strip()
            if (len(f1) != 1):
                # print(f1)
                k = len(f1)
                v1 = f1[0:k - 1]
                # print(v1)

            else:
                v1 = 1

            if (len(f2) != 1):
                # print(f2)
                k = len(f2)
                v2 = f2[0:k - 1]
                # print(v2)

            else:
                v2 = 1

        if ('-' in e1):
            items = e1.split('-')
            # print(items)

            f1 = items[0].strip()
            f2 = items[1].strip()

            if (len(f1) != 1):
                # print(f1)
                k = len(f1)
                v1 = f1[0:k - 1]
                # print(v1)

            else:
                v1 = 1

            if (len(f2) != 1):
                # print(f2)
                k = len(f2)
                v2 = f2[0:k - 1]
                str("-" + v2)
                # print(v2)

            else:
                v2 = -1

        e2 = contentEq2[0]
        str(e2)
        if ('+' in e2):
            items = e2.split('+')
            # print(items)

            f3 = items[0].strip()
            f4 = items[1].strip()

            if (len(f3) != 1):
                # print(f3)
                k = len(f3)
                v3 = f3[0:k - 1]
                # print(v3)

            else:
                v3 = 1

            if (len(f4) != 1):
                # print(f4)
                k = len(f4)
                v4 = f4[0:k - 1]
                # print(v4)

            else:
                v4 = 1

        if ('-' in e2):
            items = e2.split('-')
            # print(items)

            f3 = items[0].strip()
            f4 = items[1].strip()

            if (len(f3) != 1):
                # print(f3)
                k = len(f3)
                v3 = f3[0:k - 1]
                # print(v3)

            else:
                v3 = 1

            if (len(f4) != 1):
                # print(f4)
                k = len(f4)
                v4 = f4[0:k - 1]
                v4 =str("-" + v4)

            else:
                v4 = -1
        print(v1, v2, v3, v4)
        A = ([[int(v1), int(v2)], [int(v3), int(v4)]])
        # print(A)
        A = np.array(A).tolist()
        B = np.array([int(result1), int(result2)]).tolist()
        # print(B)
        X = np.linalg.solve(A, B)
        print("Answers : " , X)
        return X
    except:
        print("Smoothing is not Done Completely")
        return None
