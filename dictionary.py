class Dictionary:
    def __init__(self, diz):
        self.diz = diz

    def addWord(self, parola1, parola2):
        if(self.diz.get(parola1) == None):
            self.diz[parola1] = parola2
        else:
            stringa = self.diz[parola1]
            self.diz[parola1] = stringa+" "+parola2

    def translate(self, parola):
        return self.diz.get(parola)

    def translateWordWildCard(self):
        pass