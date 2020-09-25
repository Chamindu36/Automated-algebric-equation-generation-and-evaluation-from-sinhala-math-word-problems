import nltk
from nltk import tagstr2tree
from nltk.chunk.regexp import ChunkRule
from nltk.corpus import state_union, state_unionUTF
from nltk.tokenize import PunktSentenceTokenizer
import nltk
nltk.download('state_union')
from project.MathSolverRecre.Preprocessing.Tagger.TaggerUse import pos_tagging

trainSetPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/NERData.txt"
testSetPath = "D:/ZZ__FYP/project/MathSolverRecre/Preprocessing/Resources/Book.txt"
train_text = state_unionUTF.raw(trainSetPath)
sample_text = state_unionUTF.raw(testSetPath)
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = pos_tagging(words)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            gold_chunked_text = tagstr2tree(tagged)
            unchunked_text = gold_chunked_text.flatten()

            # Using chunk Grams as one at a time to get Data
            chunkGram = r"""NER: {<NN.>*<ATT>*}"""
            chunkGram1 = r"""SUBSTRACTION: {<SUB>+}"""
            chunkParser = nltk.RegexpParser(chunkGram)

            # Using ChunkRules to provide multiple regex patterns

            # chunk_Rule1 = ChunkRule("<NN.>*<ATT>*", 'NER:')
            # chunk_Rule2 = ChunkRule("<SUB>+", 'SUBSTRACTION:')
            # chunkParser1 = nltk.RegexpChunkParser([chunk_Rule1, chunk_Rule2], chunk_label="Values")
            chunked = chunkParser.parse(unchunked_text)
            print(chunked)

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()


    except Exception as e:
        print(str(e))


process_content()
