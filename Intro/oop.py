class MyClass:                              # оголошення класу                                         
    x = 10                                  # поле у класі - public static
                                            #
def demo1() -> None:                         #               
    obj1 = MyClass()                        #                   
    obj2 = MyClass()                        # особливість - оператор new не вживається
    print(obj1.x, obj2.x, MyClass.x)        # 10 10 10
    MyClass.x = 20                          # зміна поля класу - змінює у всіх об'єктах
    print(obj1.x, obj2.x, MyClass.x)        # 20 20 20
    obj1.x = 15                             # !! це не зміна, а створення(локального поля)
    print(obj1.x, obj2.x, MyClass.x)        # 15 20 20
    MyClass.x = 30                          # зміна поля класу - змінює у всіх об'єктах
    print(obj1.x, obj2.x, MyClass.x)        # 15 30 30
    obj1.w = 5                              # Склад об'єктів може змінюватись під час програми як додаватись
    obj1.y = 7                              # так і вилучатись
    del obj1.x                              #
    print(obj1.x, obj2.x, MyClass.x)        # 30 30 30 і тепер obj1.x посилається на класове
                                            #
    pass                                    #       
                                            #
class TheClass :                            # Для того щоб створити поля об'єктів, необхідний
    x = 10                                  # їх екземпляр (інстанс). він з'являється у
                                            # конструкторі. Конструктор має спеціальне ім'я __init__
    def __init__(self,                      # Покажчик "this" не є наявним у пайтон, всі методи першим
                 a=1, b:int=2) -> None:         # параметром мають його оголосити
        self.a = a                          # перегрузки методів немає
        self.b = b      
                                            # повторна декларація відміняє попередню (як пере-присвоєння). Для варіативності
        pass                                # Застосовують параметри із значенням за замовчуванням
                                            # До полів префікс self є обов'язковим
    def __str__(self) -> str:               # ToString()
        return f"A: {self.a}, B: {self.b}"
    
    def magnitude(self) -> int:             # Власні методи оголошуються за формалізмом функцій
        return self.a + self.b              # з обов'язковим параметром self

def demo2() -> None:                        # при створенні об'єктів в конструктор self передавати
    obj1 = TheClass()                       # не треба, без параметрів - за дефолтом
    print(obj1.a, obj1.b)                              
    print(obj1)
    print(TheClass(10, 20))
    print(TheClass(30))
    print(TheClass(b=40))
    print(obj1.magnitude())                 # При виклику методів self не зазначається
                                            #     
def main() -> None:                         #
    demo2()                                 #
                                            #
if __name__ == "__main__":                  #                       
    main()                                  #       