import processing
import indexing
import math


class VectorModel():
    """
    terms -> Dictionary: terms -> (doc -> times term appears in doc)
    N -> total number of documents in the system
    """

    def __init__(self, terms, N):
        self.N = N
        self.Dictionary = terms

    """
    Number of documents in which the index term ki appears
    """

    def Ni(self, Ki):
        return len(self.Dictionary[Ki])

    """
    Row frequency of term ki in the document dj (the number of times the term
    ki is mentioned in the text of the document dj)
    """

    def Freq(self, Ki, Dj):
        if Ki in self.Dictionary and Dj in self.Dictionary[Ki]:
            return self.Dictionary[Ki][Dj]
        return 0

    """
    Normalized frequency of the term ki in the document dj
    """

    def F(self, Ki, Dj):
        mod = self.modDj(Dj)
        if mod == 0:
            return 0
        return float(self.Freq(Ki, Dj)) / float(mod)

    """
    maximum over all terms which are mentioned in the text of the document dj
    """

    def MaxL(self, Dj):
        term, freq = "", 0
        for i in self.Dictionary:
            if Dj in self.Dictionary[i] and self.Dictionary[i][Dj] > freq:
                term, freq = i, self.Dictionary[i][Dj]
        return (term, freq)

    """
    Inverse document frequency for ki,
    """

    def idf(self, Ki):
        return math.log(float(self.N) / float(self.Ni(Ki)), 10)

    """
    Weight of term ki in the document Dj
    """

    def W(self, Ki, Dj):
        F = self.F(Ki, Dj)
        idf = self.idf(Ki)
        # if F == 0 or idf == 0:
        #	return 0.0
        # return (math.log(F) + math.log(idf)) * -1
        return F * idf

    """
    Weight of term ki in the query q
    """

    def Wq(self, Ki, q):
        return (0.5 + (0.5 * float(q.count(Ki)) / float(len(q)))) * self.idf(Ki)

    """
    max-frequency term in the query q
    """

    def max_Fq(self, q):
        return max([q.count(w) for w in set(q)])

    """
    Degree of similarity of the document dj with the query q
    """

    def similarity(self, dj, q):
        Wkij = sum([self.Wq(ki, dj) for ki in self.Dictionary])
        Wkiq = sum([self.Wq(ki, q) for ki in self.Dictionary])
        return (Wkij * Wkiq) / (math.sqrt(Wkij ** 2) * math.sqrt(Wkiq ** 2))

    def modDj(self, Dj):
        count = 0
        for ki in self.Dictionary:
            if Dj in self.Dictionary[ki]:
                count += self.Dictionary[ki][Dj]
        return count

    def F2(self, Ki, Dj):
        return Freq(self, Ki, Dj) / modDj(self, Dj)


class BeliefNetwork():
    """
    dict -> Dictionary: terms -> (doc -> times term appears in doc)
    docs -> Number of documents in database
    """

    def build(self, path, language, index=False):
        documents, self.language = processing.process(path, language)
        if documents is None:
            return False, self.language
        self.documents = [d for d in documents]
        self.N = len(self.documents)
        self.documents_dictionary = documents
        self.Dictionary = {}
        self.VM = VectorModel(self.Dictionary, self.N)
        for d, v in documents.items():
            for t in v:
                if t not in self.Dictionary:
                    self.Dictionary[t] = {}
                if d not in self.Dictionary[t]:
                    self.Dictionary[t][d] = 0
                self.Dictionary[t][d] += 1
        self.keys = self.Dictionary.keys()
        self.index = indexing.create(self.documents, documents, self.VM) if index else None
        self.memory = {}
        return True, self.language

    # Este método realiza la query usando el índice generado
    def query(self, query, expand_query=False):
        q = processing.process_query(query, self.language, expand_query)
        rank = self.Rank(q)
        documents = [(k, v) for k, v in rank.items() if v > 0]
        return documents, q

    def P_dj_q(self, dj, q):
        # Pk = (0.5) ** (self.N)
        Pk = 1
        S = 0
        for ki in q:
            if ki in self.Dictionary and dj in self.Dictionary[ki]:
                Pqk = self.VM.Wq(ki, q) / math.sqrt(sum([self.VM.Wq(kj, q) ** 2 for kj in q if kj in self.Dictionary]))

                if self.index:
                    Pdk = self.index[ki][dj] if ki in self.index and dj in self.index[ki] else 0
                else:
                    # Pdk = self.VM.Wq(ki, dj) / math.sqrt(sum([self.VM.Wq(kj,dj) ** 2 for kj in self.documents_dictionary[dj]]))

                    if ki in self.memory and dj in self.memory[ki]:
                        Pdk = self.memory[ki][dj]
                    else:
                        Pdk = self.VM.Wq(ki, dj) / math.sqrt(sum([self.VM.Wq(kj,dj) ** 2 for kj in self.documents_dictionary[dj]]))
                        if not ki in self.memory:
                            self.memory[ki] = {}
                        self.memory[ki][dj] = Pdk

                if Pqk != 0 and Pdk != 0 and Pk != 0:
                    S += Pqk + Pdk + Pk
                    #S += (math.log(Pqk)+math.log(Pdk)+math.log(Pk))
        return S

    def Rank(self, q):
        documents = {}
        for dj in self.documents:
            documents[dj] = self.P_dj_q(dj, q)
        return documents