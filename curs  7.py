# import curs6
# mostenirea -- inheritence
from abc import abstractmethod


class Dog:
    def __init__(self, rasa, talie, greutate, pedigree):
        self.rasa = rasa
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    def prezentare(self):
        print(f'Cainele meu este de rasa {self.rasa} si are {self.greutate} kg')


caine1 = Dog('rotwailer', 'imensa', 60, True)
caine1.prezentare()


class Shitzu(Dog):  # clasa Shitzu mosteneste clasa Dog deci are access la atribute si metode
    def __init__(self, talie, greutate, pedigree):
        self.rasa = 'Shitzu'
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    def mancare(self):
        print(f'rasa {self.rasa} mananca mancare de tipul pedigree')


caine2 = Shitzu('mica', 7, True)
caine2.prezentare()
caine2.mancare()


# polimorfism
class Husky:
    def __init__(self, talie, greutate, pedigree):
        self.rasa = 'Husky'
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    def mancare(self):  # metoda mancare exista si in clasa Shitzu, deci putem avea metode cu acelasi nume in clase diferite
        print(f'rasa {self.rasa} mananca mancare de tipul purina')


caine3 = Husky('mare', 25, True)
caine3.mancare()
caine3.greutate = 30


# abstractizare -- abstraction
class Cat:
    def __init__(self, rasa, talie, greutate, pedigree):
        self.rasa = rasa
        self.talie = talie
        self.greutate = greutate
        self.pedigree = pedigree

    @abstractmethod  # metode abstracte ce urmeaza a fi implementate in clase copil
    def mancare(self):
        pass


# incapsularea -- encapsulation
class SaveInDatabase:
    def __init__(self, tabela):
        self.__username = "Tibi"  # variabila privata care nu poate fi accesata din afara clasei
        self.__pass = "12345"
        self.tabela = tabela

    def __connection(self):  # metoda privata, nu ma pot folosi de ea in afara clasei
        print(f'conexiunea la baza de date se face cu user {self.__username} si parola {self.__pass}')

    def saveData(self, data):
        self.__connection()  # pot folosi metoda privata in clasa
        print(f"salveaza in DB aceasta data{data}")


class SaveinMyDB(SaveInDatabase):
    def sterge_user(self):
        # self.__username = "aaa"
        print(self.__username)  # nu pot accesa variabila privata din clasa parinte


# con1 = SaveInDatabase('persoane')
# print(con1.__username) #nu pot sa accesez atributul privat
# con1.__connection()

# con2 = SaveinMyDB('tabela_mea')
# con2.sterge_user()


# getere si settere
#folosim setter si getter pt a initializa si pentru a ne putea folosi de variabile private din clasa
class Sfinx(Cat):
    def __init__(self, culoare):
        self.__culoare = culoare

    @property  #initializam proprietatea variabilei private prin atnotare
    def culoare(self):
        return self.__culoare

    @culoare.getter  #atnotare pt a seta valoare variabilei private
    def culoare(self):
        return self.__culoare

    @culoare.setter  #atnotare pt a afla valoarea var private
    def culoare(self, culoare):
        self.__culoare = culoare
        print(f'culoare este {self.__culoare}')


pisica = Sfinx('alba')
pisica.culoare
pisica.culoare = "gri"
pisica.culoare

# try -- except
#folosim try -- except pt a putea trece peste o eroare care ne asteptam sa se intample
con1 = SaveInDatabase('persoane')

# print(con1.__username) #nu pot sa accesez atributul privat
try:  #punem in corpul try executia unei metode care ne asteptam sa arunce o exceptie
    con1.__connection()
except AttributeError as e:  #dupa except de regula punem eroarea care ar trebui sa se intample
    print(e)   #in corpul except putem printa ce vrem noi, chiar si eroarea care o arunca python in var e
    print("You do not have access")

try:
    print(con1.tabela)
except AttributeError as e:
    print("nu pot vedea parola")
finally:   #finally se executa dupa except in orice situatie
    print("aici ajung no matter what")


# con2 = SaveinMyDB('tabela_mea')
# con2.sterge_user()



#ex de clase ce cuprinde toate notiunile oop
class FormaGeometrica:
    @abstractmethod
    def aria(self):
        pass

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    def aria(self):
        return self.latura * self.latura

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    def aria(self):
        return 3.14 * self.raza ** 2


x = Patrat(5)
print(x.aria())
y = Cerc(4)
print(y.aria())
