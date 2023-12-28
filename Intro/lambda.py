#Лямбда-вирази: вирази, результатом яких є функції

def oper(lam) -> int:
    return lam(1,2)


def main() -> None:
    lam1 = lambda x : print(x)
    lam1('Hello')
    lam2 = lambda x,y : print(x,y)
    lam2('Hello','World')
    lam3 = lambda : print('No args')
    lam3()
    (lambda:print(10))()
    print(oper(lambda x,y : x + y))
    print(oper(lambda x,y : x - y))
    
if __name__ == '__main__' :
    main()