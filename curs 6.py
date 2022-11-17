class Persoana:   #definirea unei clase se face prin keywordul class urmat de numele clase scris cu majuscula
    nume = "Tibi"   #atribut din clasa sau o variabila locala, poate fi doar accesat nu si modificat
    sex = 'M'
    inaltime = '1.9'

    def prezentare(self):  #metoda din interiorul clasei -- self este o referinta a instantei curente din clasa adica un obiect din clasa
        print(f'Ma numesc ', self.nume, "si am inaltimea ", self.inaltime)

    #constructor
    def __init__(self, nume, sex, inaltime, varsta):  #metoda de initializare atribute din afara clasei
        self.nume = nume   #atribut ce va fi initializat la apel
        self.sex = sex
        self.inaltime = inaltime
        self.varsta = varsta


persoana1 = Persoana('Tibi', "m", '1.9', '35')   #initializarea unui obiect
print(persoana1.nume)   #folosirea unui atribut din clasa in obiectul definit
persoana1.prezentare()   #apelarea unei metode din clasa Persoana prin intermediul obiectului persoana1

persoana2 = Persoana("Ovidiu", "M", '1,84', '27')
print((persoana2.varsta))

persoana1.varsta = "31"  #am modificat atributul varsta
print(persoana1.varsta)

class Altet(Persoana):  #clasa Atlet mosteneste atribute si metode din clasa Persoana
    viteza = '12m/s'

class Angajat(Persoana): #clasa Angajat mosteneste atribute si metode din clasa Persoana
    functie = "programator"

persoana3 = Angajat
print(persoana3.nume) #putem accesa atribute din clasa mostenita