imie = 'mama'
liczba = 556
print(type(imie))
print(type(liczba))

x = imie[1:3]
imie.upper()
print(x)
'''
class Auto:
    def __init__(self, barwa, info):
    self.kolor = barwa
    self.ilosc_paliwa = 10
    self.kondycja = info
    self.tryb_ekonomiczny = False
    self.spalanie_na_100 = 14
    
a = 5
b = a
ostatecznie, prawidłowo zapisana klasa Auto:
'''
class Auto:
    def __init__(self, kolor, kondycja):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14

    def tryb_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 10

    def tryb_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0,9
        return round(zasieg)

moje_auto = Auto('czerwone', 5)
auto_Pauliny = Auto('niebieskie', 8)

print(moje_auto.kondycja)
print(auto_Pauliny.zasieg())
print(auto_Pauliny.tryb_ekonomiczny)
auto_Pauliny.tryb_eco()
print(auto_Pauliny.tryb_ekonomiczny)






