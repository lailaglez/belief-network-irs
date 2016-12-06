from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import swadesh
from nltk.corpus import stopwords
import nltk

# Procesa un fichero txt/pdf
def process(path, language=None):
    terms = []
    corpus = PlaintextCorpusReader(path, '.*')

    print(corpus.words('10'))

    if not language:
        language = identify_language(corpus)

    if not language:
        return None, 'No fue posible detectar el idioma del corpus'

    if language == 'spanish':
        stopwordlist = stopwords.words('english')
    elif language == 'english':
        stopwordlist = stopwords.words('spanish')

    print(language)

    documents = {}

    for c in corpus.fileids():
        documents[c] = [w for w in corpus.words(c) if w not in stopwordlist]
        documents[c] = nltk

    # terms = nltk.stemming(terms)
    return terms


def identify_language(corpus):
    english_words = swadesh.words('en')
    spanish_words = swadesh.words('es')

    english_count = 0
    spanish_count = 0

    for c in corpus.fileids():
        text = corpus.words(c)
        freq = nltk.FreqDist(text)

        for key in freq:
            if key.lower() in english_words:
                english_count += freq[key]
            if key.lower() in spanish_words:
                spanish_count += freq[key]

    if english_count > spanish_count:
        return 'english'
    else:
        return 'spanish'




def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)


print(process('/home/laila/Documents/texts/'))