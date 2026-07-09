Daný je neorientovaný súvislý ohodnotený graf. Pre daný štartový vrchol treba nájsť čo najdlhšiu trasu, ktorá vychádza z tohto vrcholu a cez žiadnu hranu neprechádza viackrát. Dĺžkou trasy je súčet ohodnoteních hrán. Hodnotou hrany je dĺžka úsečky (určenej koncovými bodmi), teda je to vzdialenosť dvoch bodov v rovine.

Celý graf je popísaný v textovom súbore takto:

každý riadok popisuje jeden chodník (hranu) ako štvoricu celých čísel;

každý vrchol, teda koncová súradnica hrany je dvojica celých čísel, preto je chodnik definovaný ako štvorica celých čísel x1, y1, x2, y2.

Napríklad súbor:

238 296 221 419

221 419 107 421

107 421 111 273

popisuje graf s 3 hranami, ktoré spájajú 3 vrcholy.

Metódy triedy Graf:

__init__(meno_suboru): prečíta súbor a vytvorí z neho neorientovaný ohodnotený graf reprezentovaný ako Asociatívne pole množín susedností;

je_hrana(v1, v2): vráti True, ak existuje hrana medzi týmito vrcholmi, inak vráti False; v1 a v2 sú súradnice dvoch bodov v rovine, teda sú to dvojice celých čísel;

vrcholy(): vráti množinu vrcholov (koncových vrcholov chodníkov), teda množinu dvojíc celých čísel;

start(v): pomocou backtrackingu nájde najdlhšiu trasu z vrcholu v (kde v je dvojica celých čísel); metóda vráti dvojicu: zoznam vrcholov trasy (list dvojíc celých čísel) a dĺžku trasy (súčet dĺžok hrán); ak žiadna trasa neexistuje, metóda vráti dvojicu [], 0.
