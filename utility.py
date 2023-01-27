import random as rd

def loadingSentences():
    sentences = ["Fammici pensare", "Vediamo cosa posso fare", "Certo!", "Ai tuoi ordini!", "Vediamo se mi ricordo come si fa!", "Si va in scena!"]
    return sentences[rd.randint(1, len(sentences))]


def createFolders():
    # to do
    print("...")