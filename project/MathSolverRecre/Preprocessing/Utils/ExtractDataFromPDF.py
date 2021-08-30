import PyPDF2


def readFile(filePath):
    path = str(filePath)
    outPut = []
    try:
        if (".pdf" in path):
            pdfFileObj = open(filePath, 'rb')

            # Create Reader
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            numofPages = pdfReader.numPages
            print(numofPages)

            # Create Page Object
            for i in range(numofPages):
                pageObj = pdfReader.getPage(i)
                print(pageObj)
                # Extract text from the Page
                details = pageObj.extractText()
                print(details)
                outPut.append(details)

        elif (".txt" in path):
            with open(path, "r", encoding="utf-8") as sentences_file:
            # delete_punctuation(sentences_file)
                for line in sentences_file:
                    outPut.append(line)

    except:
        print("Something went wrong")
    print(outPut)
    return outPut

# filePath = MainPath +'project/project/MathSolverRecre/Preprocessing/Resources/Book.txt'
# readFile(filePath)
