# Versin Ionela-Madalina grupa 233
import time


def tabla_numar_loc():
    """Functie pentru generarea tablei in care avem numarul trecut pe fiecare loc(locurile in care pot ajunge jucatorii)."""
    matr = [" "] * (Joc.NR_COLOANE * Joc.NR_LINII)
    # generam nr loc
    nr_loc = 0  # nr locului
    matr[18] = nr_loc
    nr_loc = nr_loc + 1
    for i in range(2, 39, 18):
        matr[i] = nr_loc
        nr_loc = nr_loc + 1
    for i in range(4, 41, 18):
        matr[i] = nr_loc
        nr_loc = nr_loc + 1
    for i in range(6, 43, 18):
        matr[i] = nr_loc
        nr_loc = nr_loc + 1
    matr[26] = nr_loc
    # generam mutarile pe care le pot face jucatorii;
    # orizontala
    for i in range(3, 6, 2):
        matr[i] = '-'
    for i in range(19, 26, 2):
        matr[i] = '-'
    for i in range(39, 43, 2):
        matr[i] = '-'
    # verticala
    for i in range(11, 16, 2):
        matr[i] = '|'
    for i in range(29, 34, 2):
        matr[i] = '|'
    # diagonala /
    for i in range(10, 17, 4):
        matr[i] = '/'
    for i in range(30, 35, 4):
        matr[i] = '/'
    # diagonala \
    for i in range(12, 17, 4):
        matr[i] = '\\'
    for i in range(28, 33, 4):
        matr[i] = '\\'
    return matr


def str_tabla(self):
    """Functie folosita pentru afisare."""
    sir = (" ".join([str(x) for x in self[0:9]]) + "\n" +
           " ".join([str(x) for x in self[9:18]]) + "\n" +
           " ".join([str(x) for x in self[18:27]]) + "\n" +
           " ".join([str(x) for x in self[27:36]]) + "\n" +
           " ".join([str(x) for x in self[36:45]]) + "\n"
           )

    return sir


def gaseste_pozitie_iepure(matrice):
    """ Functie pentru a gasi pozitia iepurelui, returneaza un tuplu cu linia si coloana pe care se afla iepurele."""
    for i in range(Joc.NR_LINII):
        for j in range(Joc.NR_COLOANE):
            if matrice[i * Joc.NR_COLOANE + j] == 'I':
                return (i, j)


def gaseste_pozitii_catei(matrice):
    "Functie folosita pentru a gasi pozitiile cateilor, returneaza o lista de tupluri"
    lista_catei = []  # lista de tupluri (linie, coloana) reprezentand pozitiile pe care se afla cateii
    for linie in range(Joc.NR_LINII):
        for coloana in range(Joc.NR_COLOANE):
            if matrice[linie * Joc.NR_COLOANE + coloana] == 'C':
                if (linie, coloana) not in lista_catei:
                    lista_catei.append((linie, coloana))
    return lista_catei


"""Dictionar in care este reprezentata distanta Manhattan de la nodul 10 (nodul pe care se afla initial iepurele), 
    la toate celelalte noduri.
    Am impartit aceasta distanta la 2 pentru a nu lua in calcul si pozitiile pe care se afla directiile.(|/-\)"""
distanta = {
    (2, 0): 4,  # nodul de pe pozitia 0
    (0, 2): 3,  # nodul de pe pozitia 1
    (2, 2): 3,  # nodul de pe pozitita 2
    (4, 2): 3,  # nodul de pe pozitita 3
    (0, 4): 2,  # nodul de pe pozitita 4
    (2, 4): 2,  # nodul de pe pozitita 5
    (4, 4): 2,  # nodul de pe pozitita 6
    (0, 6): 1,  # nodul de pe pozitita 7
    (2, 6): 1,  # nodul de pe pozitita 8
    (4, 6): 1,  # nodul de pe pozitita 9
    (2, 8): 0,  # nodul de pe pozitita 10
}


class Joc:
    NR_LINII = 5
    NR_COLOANE = 9
    SIMBOLURI_JUC = ['C', 'I']
    JMIN = None
    JMAX = None
    GOL = '*'
    MUTARI_CATEL_SUS_JOS = 0  # variabila care reprezinta numarul consecutiv de mutari sus - jos (pe verticala) ale catelusilor

    def __init__(self, tabla=None):
        # generam matricea initiala;
        if tabla is None:
            self.matr = [" "] * (Joc.NR_COLOANE * Joc.NR_LINII)
            # generam locurile in care se pot plasa jucatorii;
            for i in range(2, 7, 2):
                self.matr[i] = Joc.GOL
            for i in range(18, 27, 2):
                self.matr[i] = Joc.GOL
            for i in range(38, 43, 2):
                self.matr[i] = Joc.GOL

            # generam mutarile pe care le pot face jucatorii;
            # orizontala
            for i in range(3, 6, 2):
                self.matr[i] = '-'
            for i in range(19, 26, 2):
                self.matr[i] = '-'
            for i in range(39, 43, 2):
                self.matr[i] = '-'
            # verticala
            for i in range(11, 16, 2):
                self.matr[i] = '|'
            for i in range(29, 34, 2):
                self.matr[i] = '|'
            # diagonala /
            for i in range(10, 17, 4):
                self.matr[i] = '/'
            for i in range(30, 35, 4):
                self.matr[i] = '/'
            # diagonala \
            for i in range(12, 17, 4):
                self.matr[i] = '\\'
            for i in range(28, 33, 4):
                self.matr[i] = '\\'
            # plasam cateii pe plansa
            self.matr[18] = 'C'
            self.matr[2] = 'C'
            self.matr[38] = 'C'
            # plasam iepurele pe plansa
            self.matr[26] = 'I'
        else:
            self.matr = tabla

    def final(self):
        # cautam pozitia iepurelui
        (linie_iepure, coloana_iepure) = gaseste_pozitie_iepure(self.matr)

        # verificam daca iepurele este prins(nu mai poate sa faca nici o mutare) - astfel castiga cateii
        posibilitate_scapare = 0

        # verificam pe verticala
        if linie_iepure != 0:
            if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure] == Joc.GOL:
                posibilitate_scapare = 1
        if linie_iepure != 4:
            if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure] == Joc.GOL:
                posibilitate_scapare = 1

        # verificam pe orizontala
        if coloana_iepure != 0:
            if self.matr[linie_iepure * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                posibilitate_scapare = 1
        if coloana_iepure != 8:
            if self.matr[linie_iepure * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                posibilitate_scapare = 1

        # verificam pe diagonale
        if coloana_iepure != 0:
            if linie_iepure != 0:
                if self.matr[(linie_iepure - 1) * Joc.NR_COLOANE + coloana_iepure - 1] == '\\':
                    if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                        posibilitate_scapare = 1
            if linie_iepure != 4:
                if self.matr[(linie_iepure + 1) * Joc.NR_COLOANE + coloana_iepure - 1] == '/':
                    if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                        posibilitate_scapare = 1
        if coloana_iepure != 8:
            if linie_iepure != 0:
                if self.matr[(linie_iepure - 1) * Joc.NR_COLOANE + coloana_iepure + 1] == '/':
                    if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                        posibilitate_scapare = 1
            if linie_iepure != 4:
                if self.matr[(linie_iepure + 1) * Joc.NR_COLOANE + coloana_iepure + 1] == '\\':
                    if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                        posibilitate_scapare = 1

        # daca iepurele nu are nici o posibilitate de scapare , atunci castiga cateii
        if posibilitate_scapare == 0:
            return 'C'
        # verificam daca iepurel depaseste cateii - astfel castiga iepurele

        """ daca iepurele a ajuns pe prima coloana automat a castigat,
         sau daca catelusii au efectuat de 10 ori consecutiv mutari sus-jos (pe verticala)"""

        if coloana_iepure == 0 or Joc.MUTARI_CATEL_SUS_JOS == 10:
            return 'I'

            # verificam daca in stanga iepurelui se mai afla vreun catel
        catel_in_stanga = 0
        for i in range(Joc.NR_LINII):
            for j in range(coloana_iepure - 1, -1, -1):
                if self.matr[i * Joc.NR_COLOANE + j] == 'C':
                    catel_in_stanga += 1

        if catel_in_stanga == 0:
            return 'I'

        return False

    def mutari_joc(self, jucator):

        import copy
        l_mutari = []
        # daca jucatorul este iepure;
        # aflam pozitia iepurelui;
        if jucator == 'I':
            (linie_iepure, coloana_iepure) = gaseste_pozitie_iepure(self.matr)
            # generam toate posibilitatile de mutare ale iepurelui;

            # pe verticala jos
            if linie_iepure != 4:
                if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure] == Joc.GOL:
                    matrice_nou = copy.deepcopy(self.matr)
                    matrice_nou[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure] = 'I'
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                    l_mutari.append(Joc(matrice_nou))
            # pe verticala sus
            if linie_iepure != 0:
                if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure] == Joc.GOL:
                    matrice_nou = copy.deepcopy(self.matr)
                    matrice_nou[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure] = 'I'
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                    l_mutari.append(Joc(matrice_nou))

            # pe orizontala dreapta
            if coloana_iepure != 8:
                if self.matr[linie_iepure * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                    matrice_nou = copy.deepcopy(self.matr)
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure + 2] = 'I'
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                    l_mutari.append(Joc(matrice_nou))
            # pe orizontala stanga
            if coloana_iepure != 0:
                if self.matr[linie_iepure * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                    matrice_nou = copy.deepcopy(self.matr)
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure - 2] = 'I'
                    matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                    l_mutari.append(Joc(matrice_nou))

            # pe diagonala inapoi
            if coloana_iepure != 8:
                # pe diagonala inapoi sus
                if linie_iepure != 0:
                    if self.matr[(linie_iepure - 1) * Joc.NR_COLOANE + coloana_iepure + 1] == '/':
                        if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                            matrice_nou = copy.deepcopy(self.matr)
                            matrice_nou[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure + 2] = 'I'
                            matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                            l_mutari.append(Joc(matrice_nou))
                # pe diagonala inapoi jos
                if linie_iepure != 4:
                    if self.matr[(linie_iepure + 1) * Joc.NR_COLOANE + coloana_iepure + 1] == '\\':
                        if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure + 2] == Joc.GOL:
                            matrice_nou = copy.deepcopy(self.matr)
                            matrice_nou[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure + 2] = 'I'
                            matrice_nou[linie_iepure * Joc.NR_COLOANE + coloana_iepure] = Joc.GOL
                            l_mutari.append(Joc(matrice_nou))

            # pe diagonala inainte
            if coloana_iepure != 0:
                # pe diagonala inainte sus
                if linie_iepure != 0:
                    if self.matr[(linie_iepure - 1) * Joc.NR_COLOANE + coloana_iepure - 1] == '\\':
                        if self.matr[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                            matrice_nou = copy.deepcopy(self.matr)
                            matrice_nou[(linie_iepure - 2) * Joc.NR_COLOANE + coloana_iepure - 2] = 'I'
                            matrice_nou[(linie_iepure * Joc.NR_COLOANE + coloana_iepure)] = Joc.GOL
                            l_mutari.append(Joc(matrice_nou))
                # pe diagonala inainte jos
                if linie_iepure != 4:
                    if self.matr[(linie_iepure + 1) * Joc.NR_COLOANE + coloana_iepure - 1] == '/':
                        if self.matr[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure - 2] == Joc.GOL:
                            matrice_nou = copy.deepcopy(self.matr)
                            matrice_nou[(linie_iepure + 2) * Joc.NR_COLOANE + coloana_iepure - 2] = 'I'
                            matrice_nou[(linie_iepure * Joc.NR_COLOANE + coloana_iepure)] = Joc.GOL
                            l_mutari.append(Joc(matrice_nou))




        # generam toate posibilitatile de mutare ale cateilor
        else:
            # lista de tupluri (linie, coloana) reprezentand pozitiile pe care se afla cateii
            lista_catei = gaseste_pozitii_catei(self.matr)
            for catel in lista_catei:
                linie = catel[0]
                coloana = catel[1]

                # pe orizontala dreapta
                if coloana != 8:
                    if self.matr[linie * Joc.NR_COLOANE + coloana + 2] == Joc.GOL:
                        matrice_nou = copy.deepcopy(self.matr)
                        matrice_nou[linie * Joc.NR_COLOANE + coloana + 2] = 'C'
                        matrice_nou[linie * Joc.NR_COLOANE + coloana] = Joc.GOL
                        l_mutari.append(Joc(matrice_nou))

                # pe verticala sus
                if linie != 0:
                    if self.matr[(linie - 2) * Joc.NR_COLOANE + coloana] == Joc.GOL:
                        matrice_nou = copy.deepcopy(self.matr)
                        matrice_nou[(linie - 2) * Joc.NR_COLOANE + coloana] = 'C'
                        matrice_nou[linie * Joc.NR_COLOANE + coloana] = Joc.GOL
                        l_mutari.append(Joc(matrice_nou))
                # pe verticala jos
                if linie != 4:
                    if self.matr[(linie + 2) * Joc.NR_COLOANE + coloana] == Joc.GOL:
                        matrice_nou = copy.deepcopy(self.matr)
                        matrice_nou[(linie + 2) * Joc.NR_COLOANE + coloana] = 'C'
                        matrice_nou[linie * Joc.NR_COLOANE + coloana] = Joc.GOL
                        l_mutari.append(Joc(matrice_nou))

                # pe diagonala
                if coloana != 8:
                    if linie != 0:
                        if self.matr[(linie - 1) * Joc.NR_COLOANE + coloana + 1] == '/':
                            if self.matr[(linie - 2) * Joc.NR_COLOANE + coloana - 2] == Joc.GOL:
                                matrice_nou = copy.deepcopy(self.matr)
                                matrice_nou[(linie - 2) * Joc.NR_COLOANE + coloana - 2] = 'C'
                                matrice_nou[linie * Joc.NR_COLOANE + coloana] = Joc.GOL
                                l_mutari.append(Joc(matrice_nou))

                    if linie != 4:
                        if self.matr[(linie + 1) * Joc.NR_COLOANE + coloana + 1] == '\\':
                            if self.matr[(linie + 2) * Joc.NR_COLOANE + coloana + 2] == Joc.GOL:
                                matrice_nou = copy.deepcopy(self.matr)
                                matrice_nou[(linie + 2) * Joc.NR_COLOANE + coloana + 2] = 'C'
                                matrice_nou[linie * Joc.NR_COLOANE + coloana] = Joc.GOL
                                l_mutari.append(Joc(matrice_nou))

        return l_mutari

    def fct_euristica(self):
        """Functia care calculeaza scorul, acesta fiind reprezentat din suma  distantelor dintre
         nodurile pe care se afla jucatorii si nodul 10. Valoarea distantei se gaseste in dictionarul 'distanta'.
         Cu cat inainteaza iepurele , suma distantelor va creste, astfel scorul va fi mai mare.
         Cu cat cateii raman cat mai aproape de nodul 0 , cu atat scorul este mai mare."""
        lista_pozitii_catei = gaseste_pozitii_catei(self.matr)
        pozitie_iepure = gaseste_pozitie_iepure(self.matr)
        score = distanta[pozitie_iepure]
        for pozitie in lista_pozitii_catei:
            score += distanta[pozitie]
        return score

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (999 + adancime)
        elif t_final == Joc.JMIN:
            return (-999 - adancime)
        else:
            return self.fct_euristica()

    def __str__(self):
        sir = (" ".join([str(x) for x in self.matr[0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[9:18]]) + "\n" +
               " ".join([str(x) for x in self.matr[18:27]]) + "\n" +
               " ".join([str(x) for x in self.matr[27:36]]) + "\n" +
               " ".join([str(x) for x in self.matr[36:45]]) + "\n"
               )

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta.
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        #	(scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN


    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        print("A castigat " + final)

        return True

    return False


def main():
    timp_program_inceput = int(round(time.time() * 1000))
    # initializare algoritm
    dificultate = {"INCEPATOR": 2, "MEDIU": 5, "AVANSAT": 8}  # dictionar utilizat pentru setarea adancimii

    # DICTIONARE UTILIZATE PENTRU O CITIRE CORECTA
    # dictionar pentru noduri ,numar nod = key, value = (linie, coloana) din matrice
    dictionar_noduri = {0: (2, 0), 1: (0, 2), 2: (2, 2), 3: (4, 2), 4: (0, 4), 5: (2, 4), 6: (4, 4), 7: (0, 6),
                        8: (2, 6), 9: (4, 6), 10: (2, 8)}
    # dictionar pentru mutarile iepurelui
    dictionar_mutari_iepure = {0: [1, 2, 3], 1: [0, 2, 5, 4], 2: [0, 1, 3, 5], 3: [0, 2, 5, 6], 4: [1, 5, 7],
                               5: [1, 2, 3, 6, 9, 8, 4, 7], 6: [3, 5, 9], 7: [4, 5, 8, 10], 8: [5, 7, 9, 10],
                               9: [6, 5, 8, 10], 10: [7, 8, 9]}
    # dictionar pentru mutarile catelului
    dictionar_mutari_catei = {0: [1, 2, 3], 1: [4, 2, 5], 2: [1, 3, 5], 3: [2, 5, 6], 4: [5, 7], 5: [4, 6, 8, 7, 9],
                              6: [5, 9], 7: [8, 10], 8: [7, 9, 10], 9: [8, 10], 10: []}

    scor_JMIN = 0
    scor_JMAX = 0

    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algoritmul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-Beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Alegeti nivelul de dificultate al jocului (INCEPATOR, MEDIU, AVANSAT).").upper()
        for nivel in dificultate:
            if nivel == n:
                Stare.ADANCIME_MAX = dificultate[nivel]
                raspuns_valid = True
        if raspuns_valid == False:
            print("Trebuie sa introduceti unul dintre cuvintele din paranteza!")

    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu C sau cu I? ").upper()
        if (Joc.JMIN in ['C', 'I']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie C sau I.")
    Joc.JMAX = 'I' if Joc.JMIN == 'C' else 'C'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'C', Stare.ADANCIME_MAX)

    nr_mutari_jucator = 0
    nr_mutari_calculator = 0

    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            print("Este randul jucatorului : ", Joc.JMIN)
            nr_mutari_jucator += 1  # numaram mutarile facute de jucator

            timp_utilizator_inceput = int(round(time.time() * 1000))
            # afisam tabla cu numere
            tabla_numere = tabla_numar_loc()
            print(str_tabla(tabla_numere))

            # muta jucatorul
            raspuns_valid = False
            is_exit = 0  # variabila utilizata pentru a vedea daca a fost aleasa optiunea EXIT.
            while not raspuns_valid:
                try:
                    print("Se vor introduce numerele corespunzatoare pentru mutarea dorita. "
                          "Pentru optiunea EXIT introduceti '20' la oricare dintre cele doua elemente cerute.")
                    pozitie_curenta = int(input("Pozitia jucatorului pe care vreti sa il mutati = "))
                    if pozitie_curenta == 20:
                        is_exit = 1
                        break

                    pozitie = int(input("Pozitia unde vreti sa il mutati  = "))

                    nr_folosit_pt_validarea = 0  # numar folosit pentru validarea mutarilor
                    # (pentru a verifica ca toate conditiile sunt indeplinite)

                    if pozitie == 20:
                        is_exit = 1
                        break

                    if (pozitie in range(0, 11) and pozitie_curenta in range(0, 11)):

                        pozitie_aleasa = dictionar_noduri[pozitie]
                        pozitie_jucator = dictionar_noduri[pozitie_curenta]

                        # verificam daca pozitia pe care dorim sa mutam pionul este libera
                        if stare_curenta.tabla_joc.matr[
                            pozitie_aleasa[0] * Joc.NR_COLOANE + pozitie_aleasa[1]] == Joc.GOL:
                            nr_folosit_pt_validarea += 1
                        else:
                            print("Exista deja un simbol in pozitia ceruta.")

                        # verificam daca pozitia introdusa pt jucator (pozitia pe care se afla jucatorul) este corecta.
                        if stare_curenta.tabla_joc.matr[
                            pozitie_jucator[0] * Joc.NR_COLOANE + pozitie_jucator[1]] == Joc.JMIN:
                            nr_folosit_pt_validarea += 1
                        else:
                            print("Jucatorul nu se afla pe pozitia introdusa.")

                        # verificam daca se poate realiza mutarea (daca exista legatura intre noduri)
                        if Joc.JMIN == 'I':
                            for vecin in dictionar_mutari_iepure[pozitie_curenta]:
                                if pozitie == vecin:
                                    nr_folosit_pt_validarea += 1

                        else:
                            for vecin in dictionar_mutari_catei[pozitie_curenta]:
                                if pozitie == vecin:
                                    nr_folosit_pt_validarea += 1
                        # verificam daca toate conditiile au fost indeplinite
                        if nr_folosit_pt_validarea == 3:
                            raspuns_valid = True
                        else:
                            print("Nu se poate efectua mutarea. ")

                    else:
                        print("Pozitia pe care va aflati sau pozitia unde doriti "
                              "sa mergeti incorecta (trebuie sa fie un nr intre 0  si 10 )")

                except ValueError:
                    print("Pozitiile trebuie sa fie numere intregi")
            if is_exit:
                print("A fost aleasa optiunea EXIT!")
                scor_JMIN = stare_curenta.tabla_joc.fct_euristica()
                break

            # plasam simbolul pe "tabla de joc"
            if abs(pozitie_curenta - pozitie) == 1 and pozitie not in (0, 10) and pozitie_curenta not in (0, 10):
                Joc.MUTARI_CATEL_SUS_JOS += 1
            else:
                Joc.MUTARI_CATEL_SUS_JOS = 0

            stare_curenta.tabla_joc.matr[pozitie_aleasa[0] * Joc.NR_COLOANE + pozitie_aleasa[1]] = Joc.JMIN
            stare_curenta.tabla_joc.matr[pozitie_jucator[0] * Joc.NR_COLOANE + pozitie_jucator[1]] = '*'

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            timp_utilizator_sfarsit = int(round(time.time() * 1000))
            print("Utilizatorul a gandit si a facut mutarea in : ", timp_utilizator_sfarsit - timp_utilizator_inceput,
                  "milisecunde.")

            scor_JMIN = stare_curenta.tabla_joc.fct_euristica()  # calculeaza scorul in starea curenta

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break
            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


        # --------------------------------
        else:
            print("Este randul jucatorului : ", Joc.JMAX)
            # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            nr_mutari_calculator += 1  # numaram mutarile facute de calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            scor_JMAX = stare_curenta.tabla_joc.fct_euristica()
            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

    print("SCORUL: ", Joc.JMIN, " este ", scor_JMIN)
    print("SCORUL: ", Joc.JMAX, " este ", scor_JMAX)

    timp_program_sfarsit = int(round(time.time() * 1000))
    print("Jucatorul a efectuat ", nr_mutari_jucator, " mutari, iar calculatorul a efectuat ", nr_mutari_calculator,
          " mutari.TOTAL MUTARI: ", nr_mutari_calculator + nr_mutari_jucator)
    print("Jocul a fost jucat timp de : ", timp_program_sfarsit - timp_program_inceput, " milisecunde.")


if __name__ == "__main__":
    main()
