import nltk
nltk.download('punkt')
import nltk.tokenize


def tokenize_texts(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def tokenize_sents(text):
    tokens = nltk.sent_tokenize(text)
    return tokens

