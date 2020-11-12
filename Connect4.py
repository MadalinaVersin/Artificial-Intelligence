# Grupa 233, Versin Ionela-Madalina
import time


def elem_identice(lista):
    mt = set(lista)
    if len(mt) == 1:
        castigator = list(mt)[0]
        if castigator != Joc.GOL:
            return castigator
        else:
            return False
    else:
        return False


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 7
    NR_LINII = 6
    NR_CONNECT = 4  # cu cate simboluri adiacente se castiga
    SIMBOLURI_JUC = ['X', '0']  # ['G', 'R'] sau ['X', '0']
    JMIN = None  # 'R'
    JMAX = None  # 'G'
    GOL = '.'

    def __init__(self, tabla=None):
        self.matr = tabla or [Joc.GOL] * (Joc.NR_COLOANE * Joc.NR_LINII)

    def final(self):
        # returnam simbolul jucatorului castigator daca are 4 piese adiacente
        #	pe linie, coloana, diagonala \ sau diagonala /
        # sau returnam 'remiza'
        # sau 'False' daca nu s-a terminat jocul
        rez = False

        # verificam linii
        for linie in range(Joc.NR_LINII):
            for coloana in range(Joc.NR_COLOANE - 3):
                rez = (rez or elem_identice(
                    self.matr[linie * Joc.NR_COLOANE + coloana: linie * Joc.NR_COLOANE + coloana + 4]))

        # verificam coloane
        for coloana in range(Joc.NR_COLOANE):
            for linie in range(Joc.NR_LINII - 3):
                rez = (rez or elem_identice(self.matr[linie * Joc.NR_COLOANE + coloana: (
                                                                                                linie + 3) * Joc.NR_COLOANE + coloana + 1: Joc.NR_COLOANE]))

        # verificam diagonale \
        listaNoua = self.matr[0:41:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[1:42:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[2:35:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[3:28:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[7:40:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[14:39:8]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        # verificam diagonale /
        listaNoua = self.matr[6:37:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[13:38:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[20:39:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[5:36:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[4:29:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        listaNoua = self.matr[3:22:6]
        for i in range(len(listaNoua) - 3):
            rez = (rez or elem_identice(listaNoua[i: i + 4]))

        if (rez):
            return rez

        if rez == False and Joc.GOL not in self.matr:
            return 'remiza'
        else:
            return False

    def mutari(self, jucator_opus):
        l_mutari = []

        # folosim:
        # matr_tabla_noua = list(self.matr)
        # .... "jucator_opus" (parametrul functiei) adauga o mutare in "matr_tabla_noua"
        # l_mutari.append(Joc(matr_tabla_noua))

        import copy
        for i in range(35, 42, 1):
            if self.matr[i] == self.GOL:
                matr_tabla_noua = copy.deepcopy(self.matr)
                matr_tabla_noua[i] = jucator_opus
                l_mutari.append(Joc(matr_tabla_noua))

        for linie in range(Joc.NR_LINII - 1):
            for coloana in range(Joc.NR_COLOANE):
                if (self.matr[linie * Joc.NR_COLOANE + coloana] == self.GOL) and (
                        self.matr[(linie + 1) * Joc.NR_COLOANE + coloana] != self.GOL):
                    matr_tabla_noua = copy.deepcopy(self.matr)
                    matr_tabla_noua[linie * Joc.NR_COLOANE + coloana] = jucator_opus
                    l_mutari.append(Joc(matr_tabla_noua))

        return l_mutari

    def nr_intervale_deschise(self, jucator):
        # un interval de 4 pozitii adiacente (pe linie, coloana, diag \ sau diag /)
        # este deschis pt "jucator" daca nu contine "juc_opus"

        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX
        rez = 0

        # linii
        for linie in range(Joc.NR_LINII):
            for coloana in range(Joc.NR_COLOANE - 3):
                if juc_opus not in self.matr[linie * Joc.NR_COLOANE + coloana: linie * Joc.NR_COLOANE + coloana + 4]:
                    rez = rez + 1

        # coloane
        for coloana in range(Joc.NR_COLOANE):
            for linie in range(Joc.NR_LINII - 3):
                if juc_opus not in self.matr[linie * Joc.NR_COLOANE + coloana: (
                                                                                       linie + 3) * Joc.NR_COLOANE + coloana + 1: Joc.NR_COLOANE]:
                    rez = rez + 1

        # diagonale \

        listaNoua = self.matr[0:41:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[1:42:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[2:35:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[3:28:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[7:40:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[14:39:8]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        # diagonale /
        listaNoua = self.matr[6:37:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[5:36:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[4:29:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[3:22:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[13:38:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        listaNoua = self.matr[20:39:6]
        for i in range(len(listaNoua) - 3):
            if juc_opus not in listaNoua[i: i + 4]:
                rez = rez + 1

        return rez

    def fct_euristica(self):

        # intervale_deschisa(juc) = cate intervale de 4 pozitii
        # (pe linii, coloane, diagonale) nu contin juc_opus
        return self.nr_intervale_deschise(Joc.JMAX) - self.nr_intervale_deschise(Joc.JMIN)

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (999 + adancime)
        elif t_final == Joc.JMIN:
            return (-999 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()

    def __str__(self):
        sir = ''
        for nr_col in range(self.NR_COLOANE):
            sir += str(nr_col) + ' '
        sir += '\n'

        for lin in range(self.NR_LINII):
            k = lin * self.NR_COLOANE
            sir += (" ".join([str(x) for x in self.matr[k: k + self.NR_COLOANE]]) + "\n")
        return sir


class Stare:
    """
    Clasa folosita de algoritmii min-max si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent: " + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha >= beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break

    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    # de adagat parametru "pozitie", ca sa nu verifice mereu toata tabla,
    # ci doar linia, coloana, 2 diagonale pt elementul nou, de pe "pozitie"

    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Adancime maxima a arborelui: ")
        if n.isdigit():
            Stare.ADANCIME_MAX = int(n)
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti un numar natural nenul.")

    # initializare jucatori
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = str(input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2))).upper()
        if (Joc.JMIN in Joc.SIMBOLURI_JUC):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, Joc.SIMBOLURI_JUC[0], Stare.ADANCIME_MAX)

    linie = -1
    coloana = -1
    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    coloana = int(input("coloana = "))

                    # de verificat daca "coloana" este in intervalul corect,
                    # apoi de gasit pe ce "linie" este cea mai de jos
                    # casuta goala de pe acea "coloana"

                    if 0 <= coloana and coloana <= 6:

                        if stare_curenta.tabla_joc.matr[coloana] != Joc.GOL:
                            print("Toata coloana este ocupata.")
                        else:
                            for linie in range(Joc.NR_LINII, -1, -1):
                                if linie == 5 and stare_curenta.tabla_joc.matr[
                                    linie * Joc.NR_COLOANE + coloana] == Joc.GOL:
                                    print("Linia libera din aceasta coloana este : ", linie)
                                    raspuns_valid = True
                                    break

                                if linie < 5:
                                    if stare_curenta.tabla_joc.matr[linie * Joc.NR_COLOANE + coloana] == Joc.GOL and \
                                            stare_curenta.tabla_joc.matr[
                                                (linie + 1) * Joc.NR_COLOANE + coloana] != Joc.GOL:
                                        print("Linia libera din aceasta coloana este : ", linie)
                                        raspuns_valid = True
                                        break

                    else:
                        print("Coloana invalida (trebuie sa fie un numar intre 0 si {}).".format(Joc.NR_COLOANE - 1))

                except ValueError:
                    print("Coloana trebuie sa fie un numar intreg.")

            # dupa iesirea din while sigur am valida coloana
            # deci pot plasa simbolul pe "tabla de joc"
            pozitie = linie * Joc.NR_COLOANE + coloana
            stare_curenta.tabla_joc.matr[pozitie] = Joc.JMIN

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()



        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)

            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
