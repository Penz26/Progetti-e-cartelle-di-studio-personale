#list comprehension = un modo per creare una nuova lista con meno sintassi
#                     può emulare funzioni lambda, ma sono più leggibili
#                     list = [espressione per un oggetto in un iterabile]
#                     list = [expression for item in iterable if (conditional)]

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

#Con meno sintassi

squares = [i * i for i in range (1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,20,0]
#passed_students = list(filter(lambda x: x>=60, students))

#passed_students = [i for i in students if i >=60] fa una copia della lista con la variabile i e fa un controllo, e infine assegna questa nuova lista alla variabile
passed_students = [i if i >=60 else "Failed" for i in students ]
print(passed_students)

print()

#dictionary comprehension = crea un dizionario usando un espressione
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}


cities_in_F = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50
}

weather = {
    "New York": "Snowing",
    "Boston": "Sunny",
    "Los Angeles": "Sunny",
    "Chicago": "cloudy"
}
cities_in_C = {key: round(((value -32) * (5/9)), 2) for key,value in cities_in_F.items()}

sunny_weather_cities = {key: value for (key,value) in weather.items() if value == "Sunny"}

description_cities = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities_in_F.items()}

def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"
    
desc_cities = {key: check_temp(value) for (key,value) in cities_in_F.items()}

print(cities_in_C)
print(sunny_weather_cities)
print(description_cities)
print(desc_cities)
