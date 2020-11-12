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


<h3> Min-max algorithm and alpha-beta algorithm.</h3>
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
