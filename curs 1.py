#acesta este un comentariu
'''acesta este un
comentariu#'''

#tipuri de date
aceastaEsteVariabila = 'variabila'
variabila_int = 10
variabila_float = 10.10
variabila_bool = True
x, y, z = 1, 2, 3
print (y)
x=y=z= 10
print (z)

variabila_int = '10'
y = 'string'
print(y)

#functia type()
print(type(variabila_bool))

#functia int(), str(), bool()
motor_masina = '2000'
a = int(motor_masina)
print (a)
print (type(a))

b = str(a)
print (type(b))

automata = 0
automata = bool(automata)
print(automata)



#assert()
a = 100
b = 'ana'
assert (type(a) == int)
assert (a == 100)

#concatenare
tip_masina = 'BMW '
model_masina = 'Seria 5'
an_fabricatie = 2012
capacitate = 3000.65
masina_mea = tip_masina + model_masina
masina_ta = an_fabricatie + capacitate
print(masina_ta)


#input()
nume_masina = input('alege masina ')
print (nume_masina)

#index, len(), slicing
c = 'polimorfirsm'
print (c[2:5])
print (len(c))
print(c.upper())
print(c.lower())










