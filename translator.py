from dictionary import Dictionary
import string


class Translator:

    def __init__(self):
        pass
    def printMenu(self):
            print("1. Aggiungi nuova parola \n 2. Cerca una traduzione \n 3. Cerca con wildcard \n 4. Exit)")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        f = open(f"{dict}", "r", encoding ="utf-8")
        dizionario = {}
        for line in f:
            line = line.strip()
            lista = line.split(" ")
            dizionario[lista[0]] = lista[1]
        daTornare = Dictionary(dizionario)
        return daTornare




    def handleAdd(self, dizionario, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        lista = entry.split("> <")
        lista[0] = lista[0].replace("<", "").lower()
        lista[1] = lista[1].replace(">", "").lower()
        alfabeto = list(string.ascii_lowercase)
        true = True
        for i in range(len(lista[0])):
            if lista[0][i] not in alfabeto:
                true = False
        for i in range(len(lista[1])):
            if lista[1][i] not in alfabeto and lista[1][i]!=" ":
                true = False
        if true == False:
            print("Parola Sbagliata")
        if true == True:
            listetta = lista[1].split(" ")
            if(len(listetta)==1):
                print(f"['{lista[0]}'],['{lista[1]}']")
                dizionario.addWord(lista[0],lista[1])
            else:
                for j in range(len(listetta)):
                    dizionario.addWord(lista[0],listetta[j])
            if(len(listetta)>1):
                print(f"['{lista[0]}]',['{lista[1]}']")
            print("Aggiunta")

    def handleTranslate(self,dizionario, query):
        # query is a string <parola_aliena>
        query = query.replace("<","")
        query = query.replace(">","")
        query = query.lower()
        parola = dizionario.translate(query)
        return parola

    def handleWildCard(self,dizionario,query):
        query = query.replace("<", "")
        query = query.replace(">", "")
        query = query.lower()
        lista = []
        alfabeto = list(string.ascii_lowercase)
        for i in range(len(alfabeto)):
            parola = query.replace("?", alfabeto[i])
            datra = dizionario.translate(parola)
            if datra != None:
                lista.append(f"{parola}\n[{datra}]")
        stringa = ""
        for j in range(len(lista)):
            if(j==0):
                stringa = stringa + lista[j]
            else:
                stringa = stringa +"\n" +lista[j]
        return stringa


        # query is a string with a ? --> <par?la_aliena>
        pass