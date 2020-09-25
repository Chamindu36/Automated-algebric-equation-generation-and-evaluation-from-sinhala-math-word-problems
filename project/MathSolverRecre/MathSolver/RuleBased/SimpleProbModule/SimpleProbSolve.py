
import nltk
nltk.download('perluniprops')

def solve_simple_prob(problemType, numbers):
    numbersArray = []
    answer = 0
    for i in numbers :
        k = int(i)
        numbersArray.append(k)

    global temp3, temp2, temp1
    type = str(problemType)
    operations = type.split("/")

    if (operations[0] == "ADD"):
        temp1 = numbersArray[0] + numbersArray[1]
    elif(operations[0] == "SUB"):
        temp1 = numbersArray[0] - numbersArray[1]
    elif (operations[0] == "MUL"):
        temp1 = numbersArray[0] * numbersArray[1]
    elif (operations[0] == "DIV"):
        temp1 = numbersArray[0] / numbersArray[1]

    if (len(numbersArray)== 3):
        num3=numbersArray[2]

        if (operations[1] == "ADD"):
            temp2 = temp1 + num3
        elif(operations[1] == "SUB"):
            temp2 = temp1 - num3
        elif (operations[1] == "MUL"):
            temp2 = temp1 * num3
        elif (operations[1] == "DIV"):
            temp2 = temp1 / num3
        elif (operations[1] == "NULL"):
            temp2 = temp1
        answer = temp2

    elif (len(numbersArray) == 4):
        num3 = numbersArray[2]
        num4 = numbersArray[3]


        if (operations[1] == "ADD"):
            temp2 = temp1 + num3
        elif (operations[1] == "SUB"):
            temp2 = temp1 - num3
        elif (operations[1] == "MUL"):
            temp2 = temp1 * num3
        elif (operations[1] == "DIV"):
            temp2 = temp1 / num3
        elif (operations[1] == "NULL"):
            temp2 = temp1

        if (operations[2] == "ADD"):
            temp3 = temp2 + num4
        elif(operations[2] == "SUB"):
            temp3 = temp2 - num4
        elif (operations[2] == "MUL"):
            temp3 = temp2 * num4
        elif (operations[2] == "DIV"):
            temp3 = temp2 / num4
        elif (operations[2] == "NULL"):
            temp3 = temp2
        answer = temp3
    else:
        answer = temp1
    print(answer)
    return answer


# solve_simple_prob("MUL/ADD/MUL", [Decimal('2'), Decimal('9'), Decimal('2'), Decimal('2')])
