# functii simple
def prima_functie():  # declararea unei functii
    print('Aceasta este prima functie')  # corpul functiei


prima_functie()  # apelarea functiei


# functii cu parametrii
def functie_cu_parametrii(a):  # a este parametrul functiei
    print(f'parametrul este {a}')


functie_cu_parametrii([1, 5, 6])
functie_cu_parametrii(2)
functie_cu_parametrii('curs5')


def func_cu_2_params(a, b):  #a si b sunt parametrii deci trebuie tinut cont cand apelam functie sa ii pasam 2 valori
    c = a+b
    #print(f'suma este {a + b}')

func_cu_2_params("2", "5")
func_cu_2_params(2,5)

#functie cu multiplii parametrii
def func_cu_params_multiplii(*p):  #* se refera la un numar indefinit de parametrii care pot fi pasati functiei in momentul apelarii
    print (f'unul din paramentrii este {p[1]}')

func_cu_params_multiplii(2,4,6,"param")  #param se for stoca intr-un tuple

def functie_speciala(*masina):
    for i in masina:
        if i == "bmw":
            print(f"eu vreau eu {i}")

functie_speciala("dacia", 'opel', 'bmw')

#functie cu parametrii pasati ca si dictionar
def functie_dict(**persoane):  #** se refera la un numar indefinit de parametrii care pot fi pasati functiei in momentul apelarii
    print (f'first name is: {persoane["prenume"]}')
    print (f'last name is: {persoane["nume"]}')

functie_dict(nume='serban', prenume='tibi')  #param se vor stoca intr-un dictionar


#functie cu param default
def func_param_default(a, b = 10):  #b este un param default pt ca este initializat la crearea functiei
    print(f'suma este: {a+b}')

func_param_default(3, 5)

#functie cu parametrii de tip lista
def func_lista(lista): #paramentru care trebuie pasat la apelare este o lista din cauza corpului functiei in care se parcurge o lista
    for i in range(len(lista)):
        print (lista[i])

func_lista([1,4,7,9])  #am pasat o lista ca param


#functii cu return
def functie_return(a, b):
    return a + b  #aceasta func va returna intotdeauna o valoare

print(functie_return(10, 12)) #se va printa ce va returna functia
c = functie_return(5, 6)
print(c)


def func_retur(x, y): #functie cu return multiplu, functia se va termina cu primul return iar ce urmeaza nu va mai fi luat in considerare
    if x > y:
        return x
    else:
        return y
    return x+y #nu se va ajunge niciodata la acest return

print(func_retur(4,6))

#variabile globale si locale in functii
a = 10  #a- variabila globala
def func_var(b):  #b - parametru
    c = 15 #c -variabila locala
    return a + b + c

print(func_var(4))






