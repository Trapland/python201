import math

def homework() -> None:
    x = 0
    y = 0
    while x <= 0:
        x = input("Введіть х: ")
        x = int(x)
        if x <=0:
            print("Потрібне додатнє число")
    while y <= 0 or y == x:
        y = input("Введіть y: ")
        y = int(y)
        if y <= 0:
            print("Потрібне додатнє число")
        elif y == x:
            print("Числа повинні відрізнятись")
            
    print("%d + %d = %d" % (x, y, x+y))
    
def homework2(x,y) -> str:
    lam1 = lambda x,y : (x + y) / 2
    lam2 = lambda x,y : math.sqrt(x*y)
    lam3 = lambda x,y : 2 / (1 / x + 1 / y)
    values = [lam1(x,y), lam2(x,y), lam3(x,y)]
    if min(values) == values[0]:
        return "Arifmetic"
    elif min(values) == values[1]:
        return "Geometric"
    else:
        return "Harmonic"
    
class Fraction:
    numer:int
    denom:int

    def __init__(self,numer=0, denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self) -> str:
        return "(%d/%d)" % (self.numer,self.denom)
    
    def reduce(self):
        gcd = math.gcd(self.numer,self.denom)
        self.numer //= gcd
        self.denom //= gcd
        
def homework3() -> None:
    frac = Fraction()
    print("(no params): %s" %(frac))
    frac = Fraction(numer=5)
    print("(numer=5): %s" %(frac))
    frac = Fraction(4,6)
    print("(4,6): %s" %(frac))
    frac.reduce()
    print("Reduced: %s" %(frac))


def main() -> None:
    #homework()
    #print(homework2(1,5))
    homework3()

if __name__ == '__main__' : main()