
class myClass1():
    def method1(self):
        print("first class 1")

    def method2(self, someString):
        print("first class" + someString)

class myClass2(myClass1):
    def method1(self):
        myClass1.method1(self) #call the inherited method on the superclass
        print("second class 1")

    def method2(self, someString):
        print("second class 2")

def main():
    c = myClass1()
    c.method1()
    c.method2(" two")

    d = myClass2()
    d.method1()
    d.method2(" this is some string")


if __name__ == "__main__":
    main()
