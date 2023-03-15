class circle:
    def calcarea(self):
        r=eval(input("enter radius"))
        a=3.14*r**2
        print("Area of circle",a)
ob1=circle()
ob1.calcarea()
print(ob1)