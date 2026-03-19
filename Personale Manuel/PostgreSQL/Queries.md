#Database [[Introduzione a PostgreSQL]]
# **Grande recap delle Queries**
>Operatori, clausole, funzioni ecc...

## **1. Operatori**

| **Comando**   | **Descrizione**                                                  |
| ------------- | ---------------------------------------------------------------- |
| **`=`**       | Uguale a                                                         |
| **`<`**       | Minore di                                                        |
| **`>`**       | Maggiore di                                                      |
| **`<=`**      | Minore uguale di                                                 |
| **`>=`**      | Maggiore uguale di                                               |
| **`<>`**      | Diverso da                                                       |
| **`!=`**      | Diverso da                                                       |
| **\|\|**      | Usato per concatenare i testi di due colonne assieme             |
| **`LIKE`**    | Controlla se un valore rispetta un pattern (*CASE SENSITIVE*)    |
| **`ILIKE`**   | Controlla se un valore rispetta un pattern (*CASE INSENSITIVE*)  |
| **`AND`**     | Operatore logico e                                               |
| **`OR`**      | Operatore logico o                                               |
| **`IN`**      | Guarda se il valore della colonna rientra in una lista di valori |
| **`BETWEEN`** | Guarda se il valore della colonna è tra 2 valori                 |
| **`IS NULL`** | Controlla il valore della colonna dove è nullo                   |
| **`NOT`**     | Ritorna il contrario di altri operatori                          |

---

# **2. Proiezione dati**
> Comando **SELECT** per proiettare dati dalle tabelle in base alle specifiche che si fanno

```SQL
--Proietta i dati delle colonne customer_name e country dalla Tabella customers
SELECT customer_name, country FROM customers;

--Proietta tutti i dati delle colonne della tabella customers
SELECT * FROM customers;
```

- **SELECT DISTINCT**
>Permette di filtrare via i doppioni
>In questo caso ci mostrerà i paesi una sola volta senza i vari doppioni se ci sono dei clienti che vengono dallo stesso paese
  
```SQL
SELECT DISTINCT country FROM customers;  
```

- **SELECT COUNT(DISTINCT)**
>Conta quanti diversi dati ci sono
>Esempio: numero dei diversi paesi da cui vengono i clienti

```SQL
SELECT COUNT(DISTINCT country) FROM customers;
```

---
# **3. Selezione Dati**
>Per filtrare i dati in base a una condizione specifica usiamo la clausola WHERE

```SQL
--Il testo va tra ""
SELECT * FROM customers WHERE city = 'London';

--I valori numerici non vanno tra ""
SELECT * FROM customers WHERE customer_id = 19;

--Possiamo usare i vari operatori con la WHERE clause
SELECT * FROM customers WHERE customer_id > 80;
```

---

# **4. Ordinare i dati in ordine crescente o decrescente**
>**ORDER BY** per ordinare i risultati in ordine crescente o decrescente. 
>Di default è crescente per farlo in modo decrescente mettiamo DESC

```SQL
-- Crescente (Numeri)
SELECT * FROM products ORDER BY price;

-- Decrescente (Numeri)
SELECT * FROM products ORDER BY price DESC;

-- Ordine Alfabetico (Testo)
SELECT * FROM products ORDER BY product_name;

-- Ordine Non Alfabetico (Testo)
SELECT * FROM products ORDER BY product_name DESC;
```

>Clausola **LIMIT**
>Usato per limitare il numero di righe da ritornare

```SQL
SELECT * FROM customers LIMIT 20;
```

>Clausola **OFFSET**
>Permette di decidere da che righe iniziare a ritornare le righe

```SQL
SELECT * FROM customers LIMIT 20 OFFSET 40;
```

---
# **5. Funzioni Integrate per filtrare**

>**MIN, MAX, COUNT, SUM, AVG**
```SQL
--MIN() ritorna il valore più basso della colonna selezionata
SELECT MIN(price) FROM products;

--MAX() ritorna il valore più alto della colonna selezionata
SELECT MAX(price) FROM products;

--QUANDO SI FA MIN() MAX() LA COLONNA CHE RITORNA SI CHIAMERA' max o min di default per dargli un nome usiamo AS

SELECT MIN(price) AS lowest_price  
FROM products;
```

>**COUNT**, ritorna il numero di righe che soddisfano i filtri inseriti o semplicemente senza filtri conta le righe
```SQL
--Conta quanti customer ci sono e ne stampa il numero
SELECT COUNT(customer_id) FROM customers;

--Conta quanti customer ci sono la cui città corrisponde a London
SELECT COUNT(customer_id) FROM customers WHERE city = 'London';
```

>**SUM**, ritorna la somma numerica di una colonna con valori numerici
```SQL
SELECT SUM(quantity) FROM order_details;
```

>**AVG**, ritorna la media numerica di una colonna con valori numerici
```SQL
SELECT AVG(price) FROM products;

--Per arrotondare a solo 2 numeri decimali
SELECT AVG(price)::NUMERIC(10,2) FROM products; 
```


>**LIKE**, usato con l'operatore WHERE per cercare un preciso pattern in una colonna
>Il simbolo % rappresenta zero, uno o più caratteri
>Il simbolo _ rappresenta un singolo carattere
>**LIKE E' CASE SENSITIVE**
```SQL
--Ritorna il nome dei customer il cui nome inizia con la lettera A
SELECT * FROM customers WHERE customer_name LIKE 'A%';

--Ritorna il nome dei customer il cui nome inizia ha al suo interno la lettera A
SELECT * FROM customers WHERE customer_name LIKE '%A%';
```

>**ILIKE**, è la stessa roba di LIKE ma è CASE INSENSITIVE quindi cerca sia con lettere maiuscole o minuscole
```SQL
--Ritorna tutti i customer il cui nome contiene A oppure a
SELECT * FROM customers WHERE customer_name ILIKE '%A%';

--Ritorna tutti i customer il cui nome finisce con en
SELECT * FROM customers WHERE customer_name LIKE '%en';
```

---
# **6. Controlli in base a stringhe**

>IN, permette di specificare una lista di possibili valori per la clausola WHERE
>(Evita di concatenare più clausole OR)
```SQL
SELECT * FROM customers WHERE country IN ('Germany', 'France', 'UK');

--Può anche essere utilizzato per prendere in input i risultati di una query

--Ritorna tutti i customer che hanno un ordine nella tabella ordini
SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM orders);
```

>NOTIN, permette di ritornare tutti i record che non sono in quella lista
```SQL
SELECT * FROM customers WHERE country NOT IN ('Germany', 'France', 'UK');

--Può anche essere utilizzato per prendere in input i risultati di una query

--Ritorna tutti i customer che NON hanno un ordine nella tabella ordini
SELECT * FROM customers WHERE customer_id NOT IN (SELECT customer_id FROM orders);
```

>BETWEEN, permette di vedere i valori in un range di valori che siano stringhe, numeri o date
```SQL
--Valori Numerici
SELECT * FROM Products WHERE Price BETWEEN 10 AND 15;

--Stringhe (ritorna i valori che in ordina alfabetico sono tra quei due valori)
SELECT * FROM Products WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';

--Date (YY-MM-DD)
SELECT * FROM orders WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';
```

>AS, crea Alias per dare nomi temporanei che esistono solo per quella query
```SQL
SELECT customer_id AS id FROM customers;

--Viene anche usato nella concatenazione per unire più colonne sotto una con un singolo nome

--Proietta i nomi dei prodotti e le loro unità in una singola riga nella colonna che verrà chiamata product
SELECT product_name || unit AS product
FROM products;      
```