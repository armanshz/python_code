
class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self,string):
        print("myClass method2",string)
class anotherClass(myClass):
    def method1(self):
        # calling methods from myClass into another Class. Inherited methods can do their own thing
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self,string):
        print("anotherClass method2")

def main():
    c1 = myClass()

    c1.method1()
    c1.method2("hello")

    c2 = anotherClass()

    c2.method1()
    c2.method2("another one")

if __name__=="__main__":
    main()