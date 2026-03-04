import translator as tr
from dictionary import *

t = tr.Translator()
dizionario = t.loadDictionary("dictionary.txt")


while(True):

    t.printMenu()


    txtIn = input("Inserisci un numero: ")

    # Add input control here!

    if int(txtIn) == 1:
        parolina = input("Ok, quale parola devo aggiungere? ")
        t.handleAdd(dizionario, parolina)
    if int(txtIn) == 2:
        parolina = input("Ok, quale parola devo cercare?")
        daTradurre = t.handleTranslate(dizionario, parolina)
        print(daTradurre)
    if int(txtIn) == 3:
        parolina = input("Ok, quale parola devo cercare?")
        conteggio = 0;
        for i in range(len(parolina)):
            if parolina[i] == "?":
                conteggio += 1
        if conteggio == 1:
            stringa = t.handleWildCard(dizionario, parolina)
            print(stringa)
        else:
            print("troppi punti interrogativi")
    if int(txtIn) == 4:
        open("dictionary.txt", "w").close()
        lista = list(dizionario.diz.keys())
        listetta = []
        for i in range(len(lista)):
            stringa = lista[i] + " " + dizionario.diz.get(lista[i])
            listetta.append(stringa)
        with open("dictionary.txt", "w", encoding ="utf-8") as f:
            for i in range(len(listetta)):
                f.write(f"{listetta[i]}\n")
        break