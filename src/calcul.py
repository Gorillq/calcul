import math
import cmath

class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def min(self):
        return self.a - self.b
    def tim(self):
        return self.a * self.b
    def divd(self):
        return self.a / self.b
    
class Pow:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def power(self):
        pp = math.pow(self.m, self.n)
        return pp
    
class Root:
    def __init__(self,c):
        self.c = c
    def sqrtt(self):
        x = math.sqrt(self.c)
        return x
    def cubicsqrtt(self):
        y = math.pow(self.c, 0.33334)
        # z = math.floor(y)
        return y
    
class Complex:
    def __init__(self,d,e):
        self.d = d
        self.e = e
    def addition(self):
        return self.d + self.e
    def subs(self):
        return self.d - self.e
    def multi(self):
        return self.d * self.e
    def divi(self):
        return self.d / self.e
    
class Cmplx:
    def __init__(self,j ,k):
        self.j = j
        self.k = k
    def biegun(self):
        cm1 = cmath.polar(self.j, k)
        return cm1
    def tryg(self):
        cm2 = cmath.rect(self.j, k)
        return cm2
    def argz(self):
        cm3 = cmath.phase(self.j, k)
        return cm3
    def absolute(self):
        abss = abs(self.j, k)
        return abss
def menu():
    print("""Działania na liczbach zespolonych:
1.Dodawanie liczb zespolonych
2.Odejmowanie liczb zespolonych
3.Mnożenie liczb zespolonych
4.Dzielenie liczb zespolonych""")
    pass



print("""1.Dodawanie
2.Odejmowanie
3.Mnożenie
4.Dzielenie
5.Pierwiastek kwadratowy
6.Pierwiastek szescienny
7.Potęgowanie
8.Dzłalania na liczbach zespolonych
9.Wyjscie""")

while True:

    men = input("Wybierz co chcesz zrobic: 1-9 \n ")
    # if men is not int:
    #     xx = 0
    #     print(xx)
    NULL = ''
    if men == NULL or men >  9:
        print("Fatal Error")
        exit()
    if int(men) < 5 :
        a = input("Podaj pierwsza liczbe: \n")
        b = input("Podaj druga liczbe \n")
        obj = Calc(float(a), float(b))
        if int(men) == 1:
            print(obj.add())
        elif int(men) == 2:
            print(obj.min())
        elif int(men) == 3:
            print(obj.tim())
        elif int(men) == 4:
            koryl = obj.divd()
            value = '%.6f'%(koryl)
            print(value)
        else:
            pass
    else:
        pass

    if int(men) > 9 or NULL:
        print("Fatal Error")
        exit()
    
    if int(men) >= 5 and int(men) < 7:
        c = input("Podaj liczbe pod pierwiastkiem: \n")
        obj_2 = Root(int(c))
        if int(men) == 5:
            print(obj_2.sqrtt())
        elif int(men) == 6:
            goryl = obj_2.cubicsqrtt()
            val = '%.3f'%(goryl)
            print(val)
        else:
            pass
    else:
        pass
    
    if int(men) == 8:
        f1 = input("Podaj czesc rzeczywista pierwszej liczby: ")
        f2 = input("Podaj czesc urojona pierwszej liczby: ")
        e1 = input("Podaj czesc rzeczywista drugiej liczby: ")
        e2 = input("Podaj czesc urojona drugiej liczby: ")
        menu()
        nen = input("Wybierz opcje: \n")
        d = complex(float(f1), float(f2))
        e = complex(float(e1), float(e2))
        objn = Complex(d, e)
        if int(nen) == 1:
            print(objn.addition())
        elif int(nen) == 2:
            print(objn.subs())
        elif int(nen) == 3:
            print(objn.multi())
        elif int(nen) == 4:
            print(objn.divi())
        else:
            print("Fatal error")
    else:
        pass
    

    if int(men) == 7:
        m = int(input("Podstawa  "))
        n = int(input("Potega  "))
        obi = Pow(m, n)
        print(obi.power())
        pass
        
     
    if int(men) == 9:
        exit()

    
