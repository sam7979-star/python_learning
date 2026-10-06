class MyClass:
    var1 = "sameer"
    var2 = "Srinivasa"

    def __init__(self, dyn1, dyn2, dyn3):
        self.dyn1 = dyn1
        self.dyn2 = dyn2
        self.dyn3 = dyn3
    
    def fun1(self):
        print(f"Hello World, {self.dyn1}")
        
    def fun2(self):
        print(f"Hello World, {self.dyn2}")

    def fun3(self):
        print(f"Hello World, {self.dyn3}")

obj = MyClass("abc","xyz","lmn")
obj.fun1()
#another way to call function
MyClass.fun1(obj)