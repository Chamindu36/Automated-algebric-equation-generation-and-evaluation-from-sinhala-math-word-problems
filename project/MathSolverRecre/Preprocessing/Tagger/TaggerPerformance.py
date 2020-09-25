from nltk.corpus.reader import TaggedCorpusReader
from nltk.tag import PerceptronTagger
import math
from sklearn import metrics

from project.MathSolverRecre.Preprocessing.Tagger.PosPerceptronTagger import ngramTagger

corpus = TaggedCorpusReader("D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Tagger", r" .*\.txt", encoding="utf-16")

training_corpus = list(corpus.tagged_sents('Test_Corpus.txt'))
tagger = PerceptronTagger(load=True)

tagger.train(training_corpus)

tagged_sentences = [sentence for sentence in training_corpus]

# hold out 30% for testing
# get index for 30% split

split_idx = math.floor(len(tagged_sentences) * 0.3)
testing_sentences = tagged_sentences[0:split_idx]
training_sentences = tagged_sentences[split_idx:]

print(len(training_sentences))
print(len(testing_sentences))

# Accuracy with Unigram Tagger
tagged = PerceptronTagger(training_sentences)
Accuracy = tagged.evaluate(testing_sentences)
print('Unigram Accuracy:' + str(Accuracy))
tagged_test_sentences = tagged.tag_sents([[token for token, tag in sent] for sent in testing_sentences])
gold = [str(tag) for sentence in testing_sentences for token, tag in sentence]
prediction = [str(tag) for sentence in tagged_test_sentences for token, tag in sentence]
print(metrics.classification_report(gold, prediction))

# Accuracy with Trigram tagger
tagger = ngramTagger(training_sentences, 3, 'NNN')
print('Trigram Accuracy : ' + str(tagger.evaluate(testing_sentences)))
tagged_test_sentences = tagger.tag_sents([[token for token, tag in sent] for sent in testing_sentences])
gold = [str(tag) for sentence in testing_sentences for token, tag in sentence]
prediction = [str(tag) for sentence in tagged_test_sentences for token, tag in sentence]
print(metrics.classification_report(gold, prediction))
