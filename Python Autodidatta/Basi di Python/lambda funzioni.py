#Funzioni Lambda = funzioni scritte in una linea usando la parola chiave lambda
#                  accetta qualsiasi numero di argomenti, ma ha solo una espressione
#                  (da pensare come una scorciatoia)
#                  (utile se da usare per un corto periodo di tempo o da buttare)

#lambda parametri : espressione

#def double(x):
#    return x * 2

#print(double(5))

#Per abbreviare usiamo lambda
double = lambda x: x*2 # la prima x diventa il parametro che gli viene passato, e la seconda diventa la variabile della funzione che farà ciò che gli dice la funzione lambda
print(double(5))
multiply = lambda x, y: x * y
print(multiply(2,3))
full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Manuel", "Bernardelli"))

age_check = lambda age: True if age >= 18 else False
print(age_check(10))
