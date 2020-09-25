corpusPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Tagger/Test_Corpus.txt"
newFilePath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/WordFreq.txt"

file = open(corpusPath ,"r", encoding="utf-16")

wordcount = {}
for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
copy = []
for k, v in wordcount.items():
    copy.append((v, k))


copy = sorted(copy, reverse=True)

f2 = open(newFilePath, "w", encoding="utf8")
count = 0
for k in copy:
    count = count + k[0]
    f2.write('%s: %d' % (k[1], k[0]))
    f2.write('\n')

print(count)