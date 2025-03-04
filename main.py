import random
import operator

class Domanda:
    def __init__(self, domanda, difficolta, rispostaGiusta, risposte=[]):
        self.domanda = domanda
        self.difficolta = difficolta
        self.rispostaGiusta = rispostaGiusta
        self.risposte = risposte
        self.posizioneGiusta = 0
    def __str__(self):
        s = ""
        for i in self.risposte:
            s += str(i) + " "
        return self.domanda + "\n" + self.difficolta + "\n" + self.rispostaGiusta + "\n" + s
    def stampaRisp(self):
        s = ""
        conta = 1
        for i in self.risposte:
            s += str(conta) + ". " + str(i) + "\n"
            conta += 1
        return s

file = open("domande.txt", "r")
x = file.read()
result = x.split("\n")
listaTotale = []
conta = 0
domanda = []
for i in result:
    if i != "":
        domanda.append(i)
        conta = conta + 1
        if conta == 6:
            listaTotale.append(domanda)
            conta = 0
            domanda = []

listaDomande = []
max = 0
for i in listaTotale:
    domanda = Domanda(i[0], i[1], i[2], [i[2], i[3], i[4], i[5]])
    if int(i[1]) > max:
        max = int(i[1])
    listaDomande.append(domanda)

punteggio = 0
livelloAttuale = 0
random.shuffle(listaDomande)
domandaLiv = ""
for i in listaDomande:
    if int(i.difficolta) == livelloAttuale:
        domandaLiv = i
        print(f"Livello {livelloAttuale}) {domandaLiv.domanda} ")
        random.shuffle(domandaLiv.risposte)
        domandaLiv.posizioneGiusta = domandaLiv.risposte.index(domandaLiv.rispostaGiusta)
        print(domandaLiv.stampaRisp())
        numeroUtente = input("Inserisci la risposta: ")
        rispostaUtente = domandaLiv.risposte[int(numeroUtente) - 1]
        if livelloAttuale == max:
            break
        if rispostaUtente == domandaLiv.rispostaGiusta:
            livelloAttuale = livelloAttuale + 1
            punteggio = punteggio + 1
            print("Risposta corretta!\n")
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {domandaLiv.posizioneGiusta + 1}\n")
            break
print(f"Hai totalizzato {punteggio} punti!")

nickname = input("Inserisci il tuo nickname: ")
filePunti = open("punti.txt", "r")
y = filePunti.read()
listaRighe = y.split("\n")
dizNomi = {}
for i in listaRighe:
    if i != "":
        campi = i.split(" ")
        dizNomi[campi[0]] = int(campi[1])

entrato = False
for key in dizNomi:
    if key.lower() == nickname.lower():
        entrato = True
        dizNomi[key] = dizNomi[key] + punteggio
if not entrato:
    dizNomi[nickname] = punteggio

sorted_dizNomi = sorted(dizNomi.items(), key=operator.itemgetter(1), reverse=True)
filePunti = open("punti.txt", "w") #cancella tutto e riscrive nel file
for i in sorted_dizNomi:
    filePunti.write(f"{i[0]} {i[1]}\n")
filePunti.close()
