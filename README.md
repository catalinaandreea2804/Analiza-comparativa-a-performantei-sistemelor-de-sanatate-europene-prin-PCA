# Analiza performantei sistemelor de sanatate europene (PCA)

Acest proiect utilizeaza Analiza Componentelor Principale (PCA) pentru a evalua si compara eficienta sistemelor de sanatate din tarile europene. Studiul reduce dimensiunea setului de date pentru a identifica tipare si clusteri de tari cu performante similare.

## Indicatori utilizati
- Speranta de viata la nastere.
- Cheltuielile pentru sanatate (% din PIB).
- Numarul de medici la 100.000 de locuitori.
- Rata mortalitatii infantile.
- Procentul populatiei varstnice (65+ ani).

## Metodologie si Tehnologii
- Limbaj de programare: Python / R (pentru analiza statistica).
- Preprocesarea datelor: Normalizarea indicatorilor pentru a asigura comparabilitatea.
- Aplicarea PCA: Reducerea de la 5 dimensiuni la 2 componente principale care explica majoritatea variantei datelor.
- Vizualizare: Biplot-uri pentru interpretarea corelatiilor dintre variabile si pozitia tarilor.

## Rezultate principale
- Identificarea a doua directii de presiune asupra sistemelor de sanatate: lipsa resurselor (in tarile in curs de dezvoltare) si imbatranirea populatiei (in tarile dezvoltate).
- Clasificarea Romaniei intr-o zona de tranzitie, peste media globala, dar cu provocari legate de eficienta cheltuielilor.
- Reducerea complexitatii datelor a permis observarea unor grupari de tari imposibil de identificat prin analiza tabelelor brute.

## Utilizare
Proiectul include scriptul de analiza si setul de date procesat. Pentru rulare, este necesar un mediu capabil sa execute cod de analiza a datelor cu bibliotecile aferente (ex: scikit-learn, pandas, matplotlib sau pachetele statistice din R).
