<h1>Artificial-Intelligence <h1>
<p>These projects are performed using the A* algorithm, min-max algorithm and alpha-beta algorithm.</p>

<h3> A* algorithm.</h4>
<p><b>Problema 8-puzzle</b></p>
<p>Se da o cutie patratica 3*3 in care se gasesc 8 tablite distincte cu numere de la 1 la 8. Se dau o configuratie initiala si o configuratie finala.
Tablitele se pot muta in cutie doar prin glisarea in spatiul liber. O mutare consta, deci, dintr-o singura glisare. Se cere sa se afiseze mutarile necesare pentru a ajunge de la configuratia initiala la cea finala folosind Algoritmul A*.</p>
<p><b>Problema blocurilor</b></p>
<p>Se considera M cuburi. Fiecare cub are un identificator, de exemplu o litera.
Cuburile sunt asezate in N stive. Putem avea si stive vide (fara cuburi).
Se da o configuratie initiala a cuburilor asezate in stive si de asemenea o configuratie finala.
Se cere secventa de mutari necesara (configuratiile intermediare) pentru a ajunge de la starea initiala la starea finala. In cadrul unei mutari, nu putem lua decat un cub aflat in varful unei stive si il putem pune doar in varful unei alte stive.</p>

<p><b>Evadarea lui Mormolocel</b><p>
<p>O broscuta mica de tot statea pe o frunza la fel de mica, ce plutea alene pe suprafata unui lac. Broscuta,
spre deosebire de alte surate de-ale sale nu stia sa inoate si nu-i placea apa si poate de aceea isi dorea
tare mult sa scape din lac si sa ajunga la mal. Singurul mod in care putea sa realizeze acest lucru era
sa sara din frunza in frunza.
Forma lacului poate fi aproximata la un cerc. Coordonatele frunzelor sunt raportate la centrul acestui
cerc (deci originea axelor de coordonate, adica punctul (0,0) se afla in centrul cercului). Lungimea unei
sarituri e maxim valoarea greutatii/3. Din cauza efortului depus, broscuta pierde o unitate de
energie(greutate) la fiecare saritura. Se considera ca pierderea in greutate se face in timpul saltului,
deci cand ajunge la destinatie are deja cu o unitate mai putin. Daca broscuta ajunge la greutatea 0,
atunci moare.
Pe unele frunze exista insecte, pe altele nu. Cand broscuta ajunge pe o frunza mananca o parte din
insectele gasite si acest lucru ii da energie pentru noi sarituri. In fisierul de intrare se va specifica
numarul de insecte gasite pe fiecare frunza. Daca broscuta mananca o insecta, ea creste in greutate
cu o unitate. Atentie, odata ce a mancat o parte din insectele de pe o frunza, aceasta ramane bineinteles
fara acel numar de insecte. O tranzitie e considerata a fi un salt plus consumarea insectelor de pe
frunza pe care a ajuns.</p>


<h3> Min-max algorithm and alpha-beta algorithm.</h3>

<p><b>Connect 4</b></p>
<p>Tabla de joc are 6 linii si 7 coloane si este pozitionata vertical (perpendicular pe masa).
Se stabilesc simbolurile care vor fi folosite de fiecare dintre cei 2 jucatori (puteti folosi tot “X”
si “0”; sau “G” si “R” de la galben si rosu). Mereu muta primul jucatorul cu “X” (sau cu “G”),
 apoi cei doi muta alternativ.
Jucatorul curent isi alege o coloana (care nu este complet plina) si pune piesa cu simbolul sau
in dreptul acelei coloane. Tabla de joc fiind verticala, piesa va ajunge pe cea mai jos pozitie
libera de pe acea coloana.
Castiga jucatorul care are 4 simboluri adiacente pe linie, coloana, diagonala \ sau diagonala /.
Daca toate 42 casutele sunt completate, dar nu a castigat niciun jucator, atunci jocul se
  termina cu remiza.</p>
  
<p><b>X&0</b></p>
<p>Tabla de joc are dimensiune 3 x 3.
Cei 2 jucatori isi atribuie la inceput unul din simbolurile “X” si ”0”. Mereu prima mutare este a
jucatorului care are simbolul “X”. Cei 2 jucatori pun alternativ simbolul propriu intr-o casuta
goala.
Castiga jucatorul care are 3 simboluri adiacente pe o linie, coloana sau diagonala. Daca toate
9 casutele sunt completate, dar nu a castigat niciun jucator, atunci jocul se termina cu remiza.</p>

<p><b>HareAndHoundsGame</b></p>
<p>In acest joc sunt 3 catei si un iepure pe o tabla, pe care se deplaseaza.
 Cateii au voie sa mearga doar inainte sau pe diagonala, iar iepurele se poate deplasa si in spate.
 Iepurele va castiga daca va reusii sa se deplaseze in stanga tuturor cateilor.
 Cateii castiga daca il inconjoara pe iepure, acesta nemaiputand sa se deplaseze in nici o directie.</p>



