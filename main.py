import string

def ordina_elementi(array_coppie): # ordina le parole di ogni coppia
    n = len(array_coppie)

    for i in range(n): # ordina parole array
        p1, p2, num = array_coppie[i]
        if p1 > p2:
            array_coppie[i] = (p2, p1, num)

    for i in range(n - 1): # ordina elementi array valutando prima e seconda parola tramite selection sort
        min_index = i
        for j in range(i + 1, n):
            if array_coppie[j][0] < array_coppie[min_index][0] or (array_coppie[j][0] == array_coppie[min_index][0] and array_coppie[j][1] < array_coppie[min_index][1]):
                min_index = j

        array_coppie[i], array_coppie[min_index] = array_coppie[min_index], array_coppie[i]

    return array_coppie


def carica_parole(nome_file):
    parole = []
    with open(nome_file, 'r') as file:
        for linea in file:
            linea = linea.translate(str.maketrans('', '', string.punctuation))  # Rimuovi la punteggiatura
            parole_linea = linea.strip().split()
            parole_linea = [parola.lower() for parola in parole_linea]  # Rendi tutte le parole in minuscolo
            parole_modificate = []
            for parola in parole_linea:
                if '-' in parola:
                    parole_spezzate = parola.replace('-', ' ')
                    parole_spezzate.split()
                    parole_modificate.extend(parole_spezzate)
                    print(parole_spezzate)
                else:
                    parole_modificate.append(parola)
            parole.extend(parole_modificate)
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

def ordina_elementi(array_coppie):  # ordina le parole di ogni coppia
    n = len(array_coppie)

    for i in range(n):  # ordina parole array
        p1, p2, num = array_coppie[i]
        if p1 > p2:
            array_coppie[i] = (p2, p1, num)

    for i in range(n - 1):  # ordina elementi array valutando prima e seconda parola tramite selection sort
        min_index = i
        for j in range(i + 1, n):
            if array_coppie[j][0] < array_coppie[min_index][0] or (
                        array_coppie[j][0] == array_coppie[min_index][0] and array_coppie[j][1] <
                        array_coppie[min_index][1]):
                min_index = j

        array_coppie[i], array_coppie[min_index] = array_coppie[min_index], array_coppie[i]

    return array_coppie


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
    # print("posizioni")
    # print(posizioni)

    # coppie_distanze = calcola_distanza(frase)

    array_coppie = []

    for i in range(len(frase)):
        for j in range(i + 1, len(frase)):
            p1 = frase[i]
            p2 = frase[j]
            distanza = abs(i - j)
            if str(p1) != str(p2):
                if distanza <= 3:
                    coppia_presente = False
                    for coppia in array_coppie:
                        if (coppia[0] == p1 and coppia[1] == p2) or (coppia[0] == p2 and coppia[1] == p1):
                            coppia_presente = True
                            break
                    if not coppia_presente:
                        array_coppie.append((p1, p2, distanza))
                    else:
                        for k in range(len(array_coppie)):
                            if (array_coppie[k][0] == p1 and array_coppie[k][1] == p2) or (
                                    array_coppie[k][0] == p2 and array_coppie[k][1] == p1):
                                if array_coppie[k][2] > distanza:
                                    array_coppie[k] = (p1, p2, distanza)
                                break

    # print(array_coppie)

    distanza1, distanza2, distanza3 = 0, 0, 0
    for coppia in array_coppie:
        distanza = coppia[2]
        if distanza == 1:
            distanza1 += 1
        elif distanza == 2:
            distanza2 += 1
        elif distanza == 3:
            distanza3 += 1

    print(f'{distanza1} coppie a distanza 1')
    print(f'{distanza2} coppie a distanza 2')
    print(f'{distanza3} coppie a distanza 3')

    array_coppie_ordinate = ordina_elementi(array_coppie)

    array_due = []
    for element in array_coppie_ordinate:
        if element[2] < 3:
            array_due.append(element)
            # print("(" + str(element[0]) + "," + str(element[1]) + ") " + str(element[2]))
    # print(len(array_due))

    array_coppie_ordinate = ordina_elementi(array_coppie)
    # print(array_coppie_ordinate)

    array_due = []
    for element in array_coppie_ordinate:
        if element[2] < 3:
            array_due.append(element)
            print("(" + str(element[0]) + "," + str(element[1]) + ") " + str(element[2]))
    # print(len(array_due))

    grafo = []
    parole_frase = []

    for coppia in array_coppie_ordinate:
        if coppia[0] not in parole_frase:
            parole_frase.append(coppia[0])
        if coppia[1] not in parole_frase:
            parole_frase.append(coppia[1])

    # print(parole_frase)

    for parola1 in parole_frase:
        for parola2 in parole_frase:  # permutazione di tutte le coppie di parole
            if parola1 != parola2:
                # print(parola1, parola2)
                presente = False
                for element in grafo:
                    # controlla che la coppia non sia già nel grafo
                    if (element[0] == parola1 and element[1] == parola2) or (
                            element[0] == parola2 and element[1] == parola1):
                        # print(parola1+" "+parola2+" già presente")
                        presente = True
                        break

                if not presente:
                    # print(parola1+" "+parola2+" non presente")
                    vicini = []  # array per salvare parole adiacenti
                    adiacenti = False
                    for coppia in array_coppie_ordinate:
                        # controlla se le due parole sono adiacenti (distanza = 1)
                        if (coppia[0] == parola1 and coppia[1] == parola2 and coppia[2] == 1) or (
                                coppia[0] == parola2 and coppia[1] == parola1 and coppia[2] == 1):
                            grafo.append([parola1, parola2, coppia[2]])
                            # print("("+parola1+", "+parola2+") parole adiacenti, distanza "+str(coppia[2])+", aggiunta "+str(coppia)+" a grafo")
                            adiacenti = True
                            break

                    if not adiacenti:
                        # se le parole non sono adiacenti colleziona i vicini di parola1
                        for x in array_coppie_ordinate:
                            # if coppia[0] == parola1 and coppia[2] > 1:
                            if x[0] == parola1:  # cerca elementi del tipo (p1, _, _)
                                # print(x, x[2])
                                vicini.append(x[1])  # aggiunge _ nei vicini
                                # print("("+x[0]+", "+x[1]+") vicino > "+x[1])

                            elif x[1] == parola1:  # cerca elementi del tipo (_, p1, _)
                                # print(x, x[2])
                                vicini.append(x[0])  # aggiunge _ nei vicini
                                # print("("+x[0]+", "+x[1]+") vicino > "+x[0])

                        min_dist = 1000
                        for x in vicini:
                            for coppia in array_coppie_ordinate:
                                if (coppia[0] == x and coppia[1] == parola2) or (
                                        coppia[0] == parola2 and coppia[1] == x):
                                    if coppia[2] < min_dist:
                                        min_dist = coppia[2]

                        grafo.append([parola1, parola2, 1 + min_dist])

    # print(grafo)

    somma = 0
    max_dist = 0
    for element in grafo:
        somma += element[2]
        if element[2] > max_dist:
            max_dist = element[2]

    print("lunghezza media " + str(somma / len(grafo)))
    print("diametro " + str(max_dist))


if __name__ == '__main__':
    main()
