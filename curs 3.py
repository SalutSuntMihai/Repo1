#liste
lista_mea = ["masina", "casa", True, 22, 67.6]
#operatii cu liste
#index
print (lista_mea[4])
print((lista_mea[1::2]))
print((lista_mea[:3]))
print(lista_mea[-3:-1])

if 22 in lista_mea:
    print("valoarea este in lista")

#append
lista_mea.append(4)
print(lista_mea)

#insert
lista_mea.insert(1, "mancare")
print(lista_mea)

#change elements in list
lista_mea[1] = [10, 90, "masina"]
lista_mea[1:3] = ["da", "nu"]
print(lista_mea)

#extend
lista_2 = ['b', 'a']
lista_mea.extend(lista_2)
print(lista_mea)

#remove
lista_mea.remove(4)
print(lista_mea)

#pop
lista_mea.pop()
print(lista_mea)

#del
#del lista_mea
#print(lista_mea)

#clear
#lista_mea.clear()
#print(lista_mea)

#sort
lista_2.sort()
print(lista_2)

#copy
lista_ta = lista_mea.copy()
print(lista_ta)

#list
lista_3 = list(lista_2)
print(lista_3)

#concatenare
lista_4 = lista_2 + lista_3
print(lista_4)

#extend
lista_mea.extend(lista_2)
print(lista_mea)

#type
print(type(lista_mea))
#len
print(len(lista_mea))
#count
print(lista_mea.count('b'))

#loop list
for x in lista_mea:
    print (x)

#Dictionar
dict_meu = {
    "masina": "BMW",
    "automata": True,
}
print(dict_meu)

#indexuri bazate pe key
valoare = dict_meu["masina"]
print(valoare)
print(dict_meu.get("automata"))
#aflam keys din dictionar
print(dict_meu.keys())
#aflam valorile din dict
print(dict_meu.values())

#adaugare de elemente noi
dict_meu["culoare"] = "verde"
print(dict_meu)
#suprascriere
dict_meu["masina"] = "dacia"
print(dict_meu)

#items()
a = dict_meu.items()
print(a)
print(type(a))
print(type(dict_meu))

#check if key or value in dict
if "culoare" in dict_meu:
    print("avem culoarea " + dict_meu["culoare"])
if "dacia" in dict_meu.values():
    print("avem dacia")

#remove items
# dict_meu.pop("culoare")
# print(dict_meu)
# del dict_meu["automata"]
# print(dict_meu)
# dict_meu.clear()
# print(dict_meu)

#copiere de dict
dict_nou = dict_meu.copy()
dict_extra_nou = dict(dict_meu)
print(dict_nou)
print(dict_extra_nou)

#nested dict
dict_tau = {
    "copil1": {
        "nume": "natalia",
        "ani": 1
    },
    "copil2": {
        "nume": "Sofia",
        "ani": 2
    }
}
#len
print(len(dict_tau))

#tuples
my_tuple = ("dacia", "bmw", 2)
print(my_tuple[1])
#workaround pt a adauga element nou
x = list(my_tuple)
x[1] = "renault"
my_tuple = tuple(x)
print(my_tuple)
#concatenare
tuple_nou = ("bmw", 4)
tuple_nou = my_tuple + tuple_nou
print(tuple_nou)
#len
print(len(tuple_nou))

#seturi
my_set = {"masina", "casa", 12}
#accesare valori
for x in my_set:
    print(x)
#adaugare element
my_set.add(False)
print((my_set))
#stergere element
my_set.remove("casa")
print(my_set)
my_set.pop()
print(my_set)
my_set.discard(12)
#update
set_nou = {1,2,3}
my_set.update(set_nou)
print(my_set)


