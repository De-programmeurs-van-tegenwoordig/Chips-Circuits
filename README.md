# Chips-Circuits

## Case
De case bestaat uit het vormen van een chip. De chip bestaat uit verschillende gates die op een bepaalde manier met elkaar verbonden staan. Deze manier komt voort uit de netlist.

### Voorbeeld:
##### Chip bestaat uit gates:

| chip | coordinaten |
|---|---|
| 1 | (1,5) |
| 2 | (6,5) |
| 3 | (4,4) |
| 4 | (6,2) |
| 5 | (3,1) |

##### En de gates moeten verbonden zijn volgens de netlist:
| chip_a | chip_b |
|---|---|
| 1 | 2 |
| 1 | 3 |
| 3 | 5 |
| 4 | 2 |
| 4 | 5 |

##### Wat er vervolgens op deze manier uit komt te zien:
![Voorbeeld chip 0 netlist 1:](Graphs/Astar/0/1/shortest/Shortest.png)

### Echter zijn er constricties waaraan voldaan moet worden
* Draden mogen niet overlappen
* Draden mogen niet door andere gates heenlopen
* Het kruizen van draden mag, maar kost 300

## Oplossingen
Voor deze case zijn verschillende algoritmes van toepassing. Hierbij hebben wij gekozen voor deze algoritmes:
* Random
* Greedy
* A*

## Random
Bij dit algoritme wordt bij elke stap van het leggen van een draad een willekeurige directie gepakt. Dit is een mogelijke oplossing voor de eerste chip en zijn netlists, maar zodra
er meer kabels en meer gates bijkomen, kan het random algoritme niet meer tot een oplossing komen. 

## Greedy
Bij dit algoritme wordt bij elke stap van het leggen van een draad de afstand tussen het doel en het huidige punt berekent, en zo de meest optimale directie te bepalen.
Dit zorgt ervoor dat bij kleinere chips de meest lage kosten tevoorschijn komen, en dat grotere chips en netlist wel tot een oplossing kunnen komen. Echter de meest
lastige chip en netlists kan greedy niet oplossen, omdat hij zichzelf vastloopt.

## A*
Bij dit algoritme wordt bij elke stap gekeken naar de afstand tussen het doel en het huidige punt, maar wordt elke mogelijke richting die eerder nog open stond opgeslagen, zodat 
wanneer de lijn vast komt te liggen hij altijd nog terug kan naar een eerdere directie. Dit zorgt ervoor dat de moeilijkste chips en netlist een oplossing kan krijgen. Bij dit algoritme
wordt het kruizen van kabels zo veel mogelijk voorkomen (tenzij er geen andere mogelijkheid is), om zo kosten te minimaliseren. 

