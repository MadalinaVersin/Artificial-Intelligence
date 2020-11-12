# Versin Ionela-Madalina grupa 233

""" Definirea problemei """
import math
from time import perf_counter


def distanta(x1, y1, x2, y2):
    """Functie care calculeaza distanta dintre 2 puncte."""
    x = x2 - x1
    y = y2 - y1
    rezultat = math.sqrt(((x) ** 2) + ((y) ** 2))
    return rezultat


class Nod:
    def __init__(self, info, h):
        self.info = info  # info este un tuplu de forma ("identificator frunza",coordonata_x, coordonata_y, nr_insecte, greutate_maxima,greuatate_broasca)
        self.h = h  # h reprezinta distanta de la frunza la mal

    def __str__(self):
        return "{}({}, {})".format(self.info[0], self.info[1], self.info[2])

    def __repr__(self):
        return f"{self.info[0]}({self.info[1]}, {self.info[2]})"


def fct_h(frunza_curenta_x, frunza_curenta_y, raza):
    """Functia care il calculeaza pe h."""
    return raza - distanta(frunza_curenta_x, frunza_curenta_y, 0, 0)


class Problema:

    def __init__(self, raza, greutate, id_frunza_start, frunze):
        self.raza = raza  # reprezinta raza lacului
        self.greutate = greutate  # greutatea initiala a broscutei
        self.id_frunza_start = id_frunza_start  # id-ul frunzei initiale
        self.frunze = frunze  # o lista de tupluri de forma(id_frunza,coordonata_x, coordonata_y, nr_insecte_de_pe_frunza,greutatea_maxima_admisa_de_frunza)

        for frunza in self.frunze:  # cautam nodul start

            if frunza[0] == self.id_frunza_start:
                self.nod_start = Nod((frunza[0], frunza[1], frunza[2], frunza[3], frunza[4], self.greutate),
                                     fct_h(frunza[1], frunza[2], self.raza))


def cauta_nod_nume(self, info):
    """Functie care cauta un nod care informatia "info" , daca aceasta este gasita se returneaza nodul , altfel se returneaza None"""
    for frunza in self.frunze:
        if frunza.info == info:
            return frunza
    return None


""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf

    """

    problema = None  # atribut al clasei

    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip Nod
        self.g = g  # costul drumului de la radacina pana la nodul curent, reprezentat prin numarul de sarituri
        if f is None:
            self.f = self.g + self.nod_graf.h  # f este costul estimat al unui drum
        else:
            self.f = f

    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina.
        """

        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def expandeaza(self):
        """Pentru nodul curent , cautam toti succesorii (fiii) sai .Se va returna o lista de tupluri
         de forma(nod_fiu, cost_muchie_tata_fiu), sau o lista vida daca nodul curent nu are succesori"""
        l_succesori = []
        if self.nod_graf.info[5] > 0:  # testam daca greutatea broscutei este 0

            for frunza in self.problema.frunze:  # luam toate frunzele
                if self.nod_graf.info[0] != frunza[
                    0]:  # testam ca frunza_curenta sa fie diferita de frunza pe care dorim sa sarim
                    insecte_mancate = self.nod_graf.info[
                        3]  # cu cat mananca mai multe insecte cu atat poate sa sara mai mult.
                    while insecte_mancate >= 0:  # vedem in functie de insectele mancate daca poate sa ajunge pe frunza(frunza pe care vrea sa sara)
                        if self.nod_graf.info[5] + insecte_mancate <= frunza[4] and (
                                self.nod_graf.info[5] + insecte_mancate) / 3 >= distanta(self.nod_graf.info[1],
                                                                                         self.nod_graf.info[2],
                                                                                         frunza[1],
                                                                                         frunza[2]):
                            """Daca sunt indeplinite conditiile ca noua greutate a broscutei sa fie mai mica decat greutatea maxima admisa de frunza  pe care va sari 
                            si noua greuatate / 3 sa fie mai mare decat distanta dintre cele 2 frunze, atunci frunza este 
                            adaugata in lista de succesori 


                            """

                            greutate_nou = self.nod_graf.info[5] + insecte_mancate - 1
                            frunza_nou = Nod((frunza[0], frunza[1], frunza[2], frunza[3], frunza[4], greutate_nou),
                                             fct_h(frunza[1], frunza[2], self.problema.raza))
                            l_succesori.append((frunza_nou, 1))
                        insecte_mancate = insecte_mancate - 1

        return l_succesori

    def test_scop(self):
        # verificam daca exista posibilitatea de a sari de pe frunza curenta pe mal .
        for insecte_mancate in range(self.nod_graf.info[3] + 1):
            if self.nod_graf.h <= (self.nod_graf.info[5] + insecte_mancate) / 3:
                return 1
        return 0


""" Algoritmul A* """


def str_info_noduri(l):
    """
        O functie folosita strict in afisari
    """
    sir = ""
    if len(l) != 1:
        # cazul in care nodul de start nu este si nodul scop
        for i in range(len(l) - 1):
            nr_insecte_mancate = l[i + 1].nod_graf.info[5] - l[i].nod_graf.info[5] + 1
            if i == 0:
                sir += str(i + 1) + ")Broscuta se afla pe frunza initiala " + str(l[i].nod_graf) + "."
                sir += "Broscuta a mancat " + str(nr_insecte_mancate) + " insecte."
                sir += "Greutate broscuta: " + str(l[i].nod_graf.info[5] + nr_insecte_mancate)
            else:
                sir += str(i + 1) + ")Broscuta a sarit de la " + str(l[i - 1].nod_graf) + " la " + str(
                    l[i].nod_graf) + ". "
                sir += "Broscuta a mancat " + str(nr_insecte_mancate) + " insecte. "
                sir += "Greutate broscuta: " + str(l[i].nod_graf.info[5] + nr_insecte_mancate)
            sir += '\n'
        i = len(l) - 1
        for insecte_mancate in range(l[i].nod_graf.info[3], -1, -1):
            if (distanta(l[i].nod_graf.info[1], l[i].nod_graf.info[2], 0, 0) + (
                    (l[i].problema.greutate + insecte_mancate) / 3)) >= l[i].problema.raza:
                sir += str(i + 1) + ")Broscuta a sarit de la " + str(l[i - 1].nod_graf) + " la " + str(
                    l[i].nod_graf) + ". "
                sir += "Broscuta a mancat " + str(insecte_mancate) + " insecte. "
                sir += "Greutate broscuta: " + str(l[i].nod_graf.info[5] + insecte_mancate)
                sir += "\n"
                break
    else:
        # utilizata in cazul in care nodul start este si nodul scop
        i = len(l) - 1
        for insecte_mancate in range(l[i].nod_graf.info[3], -1, -1):
            if (distanta(l[i].nod_graf.info[1], l[i].nod_graf.info[2], 0, 0) + (
                    (l[i].problema.greutate + insecte_mancate) / 3)) >= l[i].problema.raza:
                sir += str(i + 1) + ")Broscuta a sarit de la " + str(l[i].nod_graf) + " la mal. "
                if insecte_mancate != 0:
                    sir += str(i + 1) + ")Broscuta a mancat " + str(insecte_mancate) + " insecte. "
                sir += "Greutate broscuta: " + str(l[i].nod_graf.info[5] + insecte_mancate)
                sir += "\n"
                break

    sir += str(len(l) + 1) + ")Broscuta ajuns la mal in " + str(l[len(l) - 1].g + 1) + " sarituri."
    sir += "\n"
    return sir


def afis_succesori_cost(l):
    """
        O functie folosita strict in afisari
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)
    return sir


def in_lista(l, nod):
    """
        Lista "l" contine obiecte de tip NodParcurgere
        "nod" este de tip Nod
    """
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None


def a_star():
    """
        Functia care implementeaza algoritmul A-star
    """

    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
    closed = []  # closed va contine elemente de tip NodParcurgere

    while len(open) > 0:
        print(str_info_noduri(open))  # afisam lista open
        nod_curent = open.pop(0)  # scoatem primul element din lista open
        closed.append(nod_curent)  # si il adaugam la finalul listei closed

        # testez daca nodul extras din lista open este nod scop (si daca da, ies din bucla while)
        if nod_curent.test_scop():
            break

        l_succesori = nod_curent.expandeaza()  # contine tupluri de tip (Nod, numar)

        for (nod_succesor, cost_succesor) in l_succesori:
            # "nod_curent" este tatal, "nod_succesor" este fiul curent

            # daca fiul nu e in drumul dintre radacina si tatal sau (adica nu se creeaza un circuit)
            if (not nod_curent.contine_in_drum(nod_succesor)):

                # calculez valorile g si f pentru "nod_succesor" (fiul)
                g_succesor = nod_curent.g + cost_succesor  # g-ul tatalui + cost muchie(tata, fiu)
                f_succesor = g_succesor + nod_succesor.h  # g-ul fiului + h-ul fiului

                # verific daca "nod_succesor" se afla in closed
                # (si il si sterg, returnand nodul sters in nod_parcg_vechi
                nod_parcg_vechi = in_lista(closed, nod_succesor)

                if nod_parcg_vechi is not None:  # "nod_succesor" e in closed
                    # daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
                    # 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista closed)
                    # atunci actualizez parintele, g si f
                    # si apoi voi adauga "nod_nou" in lista open
                    if (f_succesor < nod_parcg_vechi.f):
                        closed.remove(nod_parcg_vechi)  # scot nodul din lista closed
                        nod_parcg_vechi.parinte = nod_curent  # actualizez parintele
                        nod_parcg_vechi.g = g_succesor  # actualizez g
                        nod_parcg_vechi.f = f_succesor  # actualizez f
                        nod_nou = nod_parcg_vechi  # setez "nod_nou", care va fi adaugat apoi in open

                else:
                    # daca nu e in closed, verific daca "nod_succesor" se afla in open
                    nod_parcg_vechi = in_lista(open, nod_succesor)

                    if nod_parcg_vechi is not None:  # "nod_succesor" e in open
                        # daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
                        # 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista open)
                        # atunci scot nodul din lista open
                        # 		(pentru ca modificarea valorilor f si g imi va strica sortarea listei open)
                        # actualizez parintele, g si f
                        # si apoi voi adauga "nod_nou" in lista open (la noua pozitie corecta in sortare)
                        if (f_succesor < nod_parcg_vechi.f):
                            open.remove(nod_parcg_vechi)
                            nod_parcg_vechi.parinte = nod_curent
                            nod_parcg_vechi.g = g_succesor
                            nod_parcg_vechi.f = f_succesor
                            nod_nou = nod_parcg_vechi

                    else:  # cand "nod_succesor" nu e nici in closed, nici in open
                        nod_nou = NodParcurgere(nod_graf=nod_succesor, parinte=nod_curent, g=g_succesor)
                    # se calculeaza f automat in constructor

                if nod_nou:
                    # inserare in lista sortata crescator dupa f
                    # (si pentru f-uri egale descrescator dupa g)
                    i = 0
                    while i < len(open):
                        if open[i].f < nod_nou.f:
                            i += 1
                        else:
                            while i < len(open) and open[i].f == nod_nou.f and open[i].g > nod_nou.g:
                                i += 1
                            break

                    open.insert(i, nod_nou)

    print("\n------------------ Concluzie -----------------------")
    if len(open) == 0:
        if rad_arbore.test_scop():
            gout.write(str_info_noduri([rad_arbore]))
        else:
            gout.write("Lista open e vida, nu avem drum de la nodul start la mal.\n")
    else:
        gout.write("Drum de cost minim: \n" + str_info_noduri(nod_curent.drum_arbore()))


if __name__ == "__main__":
    lista_fisiere_input = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt"]  # lista fisiere input
    lista_fisiere_output = ["output_1.txt", "output_2.txt", "output_3.txt", "output_4.txt"]  # lista fisiere output
    for fisier in range(len(lista_fisiere_input)):
        timp_initial = perf_counter()
        f = open(lista_fisiere_input[fisier], "r")
        frunze = []
        line = f.readline()  # citeste raza din fisier
        raza = int(line)
        line = f.readline()  # citeste greutatea initiala a broscutei din fisier
        greutate = int(line)
        line = f.readline()  # se citeste id-ul frunzei start
        id_frunza_start = line.strip()
        line = f.readline()  # se citeste prima frunza

        while line != "":  # citeste toate frunzele dintr-un fisier
            caracteristici_frunza = line.split(" ")
            frunza = (str(caracteristici_frunza[0]), int(caracteristici_frunza[1]), int(caracteristici_frunza[2]),
                      int(caracteristici_frunza[3]), int(caracteristici_frunza[4]))
            frunze.append(frunza)
            line = f.readline()

        f.close()

        problema = Problema(raza, greutate, id_frunza_start, frunze)
        NodParcurgere.problema = problema
        gout = open(lista_fisiere_output[fisier], "w")
        a_star()
        timp_final = perf_counter()

        gout.write("Programul a rulat : " + str(timp_final - timp_initial) + " milisecunde.")

        gout.close()



