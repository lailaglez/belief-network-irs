from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import swadesh
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import nltk
import os


language_dic = {'english': 'en', 'spanish': 'es', 'german': 'de', 'french': 'fr', 'italian': 'it', 'portuguese': 'pt'}
languages_available = language_dic.keys()

# Procesa un fichero txt/pdf
def process(path, language=None):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                os.system("pdftotext " + str(os.path.join(root, file) + " " + str(os.path.join(root, file)[:-4]) + ".txt"))

    corpus = PlaintextCorpusReader(path, '.*\.txt')

    if not language:
        language = identify_language(corpus)

    if not language:
        return None, 'No fue posible detectar el idioma del corpus'

    stopwordlist = stopwords.words(language)
    punctuation = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                   '=', '+', '{', '}', '[', ']', ';', ';', ':', '"', "'", ',', '.', '<', '>', '?', '/']

    documents = {}
    stemmer = nltk.SnowballStemmer(language)

    for c in corpus.fileids():
        documents[c] = [stemmer.stem(w) for w in corpus.words(c) if w not in stopwordlist and w not in punctuation]
        title = c[:-4].split()
        documents[c].extend([stemmer.stem(w) for w in title])

    # Retorna un diccionario {nombre del documento: lista de términos en el documento}
    # y una lista con los términos de la query procesada
    return documents, language


def identify_language(corpus):
    s_ratio = stopwords_ratio(corpus)
    c_ratio = common_words_ratio(corpus)

    return max([(s_ratio[l] + c_ratio[l], l) for l in language_dic])[1]


def stopwords_ratio(corpus):
    ratio = {}

    for language in language_dic:
        ratio[language] = 0
        stopwords_set = set(stopwords.words(language))
        for c in corpus.fileids():
            word_set = set(corpus.words(c))
            ratio[language] += len(stopwords_set.intersection(word_set))

    return ratio


def common_words_ratio(corpus):
    ratio = {}

    for language, value in language_dic.items():
        ratio[language] = 0
        for c in corpus.fileids():
            swadesh_set = set(swadesh.words(value))
            word_set = set(corpus.words(c))
            ratio[language] += len(swadesh_set.intersection(word_set))

    return ratio


def process_query(query, language):
    query = query.split()
    result = query.copy()

    for q in query:
        ss = wordnet.synsets(q)
        if len(ss) == 1:
            for l in ss[0].lemmas():
                result.extend(l.name().split('_'))

    stemmer = nltk.SnowballStemmer(language)
    stopwordlist = stopwords.words(language)

    return [stemmer.stem(w) for w in result if w not in stopwordlist]


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)