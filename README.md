## Rekurzivní implementace Fibonnaciho posloupnosti
Výchozími prvky posloupnosti jsou hodnoty 0 a 1. Celá posloupnost se tvoří tak, že každé další číslo vznikne součtem 
dvou předcházejících. Vznikne tedy řada: 0, 1, 1, 2, 3, 5, 8, 13, 21,...

Fibonacciho posloupnost opět můžeme popsat několika způsoby. Pro následnou implementaci rekurzivního algoritmu se pak 
hodí zejména:

* *f(n)* = 0, pokud *n* = 0,
* *f(n)* = 1, pokud *n* = 1,
* *f(n)* = *f(n - 1)* + *f(n - 2)*, jinak.

## Rekurzivní implementace binárního vyhledávání
Jde o způsob prohledávání zadaného prostoru, seřazeného číselného seznamu, za účelem nalezení specifické hodnoty. 
Tento algoritmus můžeme implementovat pomocí rekurze. Připomeneme si princip algoritmu:

* Zkontroluj prostřední prvek. Pokud obsahuje hledanou hodnotu, ukonči hledání a vrať pozici prostředního prvku.
* Pokud je prostřední prvek menší než hledané číslo, zmenši oblast prohledávání na pravou půlku seznamu.
* Pokud je prostřední prvek větší než hledané číslo, zmenši oblast prohledávání na levou polovinu seznamu.
* Opakuj předchozí kroky dokud existuje oblast, která ještě nebyla prohledána. 

Rekurzivní přístup přichází na řadu v momentu krácení prohledávaného prostoru na polovinu (ať už levou, nebo pravou).

## Semínkové vyplňování (flood fill)
[Flood fill](https://en.wikipedia.org/wiki/Flood_fill) je algoritmus, který určuje a mění oblast připojenou k danému 
uzlu ve vícerozměrném poli na základě nějakého společného atributu. Typickým využitím je nalezení spojené komponenty 
v obraze, což můžete znát z nejrůznějších kreslících programů jako nástroj vyplnit oblast (kyblík s barvou). 

Algoritmus začíná ze zvoleného semínka, odkud se nová barva šíří všemi směry do dalších pixelů, pokud mají pixely 
stejnou barvu jako má semínko. 

Algoritmus je velmi vhodný pro rekurzivní implementaci - semínko může rozšířit svou barvu na okolní pixely a ty můžou 
rekurzivně rozšířit svou barvu na své okolí. Postup bude tedy následující:

* Pro aktuální pixel zkontroluj, zda leží uvnitř v obraze (pozice se nedostala mimo velikost obrazu) a zda je zelený. 
  Pokud ne, tak vrať nezměněný obraz.
* Změň barvu aktuální pixelu na červenou.
* Zavolej tuto funkci rekurzivně pro sousední pixely.
* Vrať upravený obraz.
