import re


# Remove Unnecessary Characters
def remove_characters(self, text):
    cyril = re.compile(u'[\u0021-\u007F]', re.UNICODE)

    plainText = cyril.sub('', str(text))

    return plainText


def delete_punctuation(sentences):
    text = ''.join(sentences)

    punctuations = ['(', ')', "***", ';', ',', '.', '!', '"', "'", "#", "...", "..", "-", "!", "@", "^"]

    for word in text.split():
        for chars in word:
            if chars in punctuations:
                word1 = word.replace(chars, ' ')
                text = text.replace(word, word1)
    return text
