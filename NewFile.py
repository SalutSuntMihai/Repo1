from abc import abstractmethod
sold= float(5599.45)
nume= 'Dan'
prenume= 'Barna'
activ= True

class ContBancar1():
    def __init__(self,sold,nume,prenume,activ):
        self.sold=sold
        self.nume=nume
        self.prenume=prenume
        self.activ=activ
    def PrezentareSold(self):
        if self.activ == True:
            print(f'{self.nume} {self.prenume} aveti {self.sold} lei')
        else:
            print('Contul dumneavoastra este inactiv')
x= ContBancar1(233,'mirc','z',True)
x.PrezentareSold()

class ContBancar2(ContBancar1):
    def __init__(self,sold, nume, prenume, activ):
        self.sold= 20
        self.nume= nume
        self.prenume = prenume
        self.activ = activ
c=ContBancar2(20,'adasd','cur',True)
c.PrezentareSold()
