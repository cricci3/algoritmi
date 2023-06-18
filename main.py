import string


def carica_parole(nome_file):
    parole = []
    with open(nome_file, 'r') as file:
        for linea in file:
            linea = linea.translate(str.maketrans('', '', string.punctuation))  # Rimuovi la punteggiatura
            parole_linea = linea.strip().split()
            parole_linea = [parola.lower() for parola in parole_linea]  # Rendi tutte le parole in minuscolo
            parole.extend(parole_linea)
    return parole


def calcola_distanza(parole):
    distanze = []

    # Calcola la distanza tra tutte le coppie di parole con distanza <= 3
    for i in range(len(parole) - 1):
        for j in range(i + 1, min(i + 4, len(parole))):
            distanza = abs(j - i)
            distanze.append((parole[i], parole[j], distanza))

        # Rimuovi coppie di parole con distanze diverse ma con le stesse parole
        coppie_distanze_univoche = []
        parole_esistenti = set()
        for coppia in distanze:
            parola1, parola2, distanza = coppia
            if (parola1, parola2) not in parole_esistenti and (parola2, parola1) not in parole_esistenti:
                coppie_distanze_univoche.append(coppia)
                parole_esistenti.add((parola1, parola2))

        return coppie_distanze_univoche


def main():
    nome_file = 'Testi//esempio00.txt'
    frase = carica_parole(nome_file)

    parole = {}
    for parola in frase:
        if parola in parole:
            parole[parola] += 1
        else:
            parole[parola] = 1

    numero_parole_diverse = len(parole)
    numero_totale_occorrenze = sum(parole.values())

    print(f"{numero_parole_diverse} parole")
    print(f"{numero_totale_occorrenze} occorrenze")
    print()

    parole_frequenti = sorted(parole.items(), key=lambda x: (-x[1], x[0]))[:20]

    # Stampa parole con occorrenza in ordine decrescente
    for parola, frequenza in parole_frequenti:
        print(parola, frequenza)

    posizioni = []
    count = 1
    # Definisci la posizione di ogni parola nella frase
    for parola in frase:
        posizioni.append([parola, count])
        count += 1
    print("posizioni")
    print(posizioni)

    coppie_distanze = calcola_distanza(frase)
    conteggio_distanze = {1: 0, 2: 0, 3: 0}

    for coppia in coppie_distanze:
        parola1, parola2, distanza = coppia
        if distanza <= 3 and parola1 != parola2:
            print(parola1 + ",", parola2 + ",", distanza)
            conteggio_distanze[distanza] += 1

    print("Numero di coppie a distanza 1:", conteggio_distanze[1], "coppie")
    print("Numero di coppie a distanza 2:", conteggio_distanze[2], "coppie")
    print("Numero di coppie a distanza 3:", conteggio_distanze[3], "coppie")


if __name__ == '__main__':
    main()
