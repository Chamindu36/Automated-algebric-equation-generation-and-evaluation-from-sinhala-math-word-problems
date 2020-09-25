import pickle
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import TaggedCorpusReader


def ngramTagger(train_sents, n=3, defaultTag='NN'):
    t0 = nltk.DefaultTagger(defaultTag)
    if (n <= 0):
        return t0
    elif (n == 1):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        return t1
    elif (n == 2):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        return t2
    else:
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        t3 = nltk.TrigramTagger(train_sents, backoff=t2)
        return t3

#Get Corpus from resources
corpus_1 = TaggedCorpusReader("D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Tagger", r" .*\.txt", encoding="utf-16")

training_corpus = list(corpus_1.tagged_sents('Test_Corpus.txt'))
tagger = nltk.PerceptronTagger(load=True)
#
# Unigram perceptron tagger initiation
tagger.train(training_corpus)
save_tagger = open("perceptron_tagger.pickle", "wb")
pickle.dump(tagger, save_tagger)
save_tagger.close()
