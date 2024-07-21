# oops part2

# del keyword:
# used to delete object properties or object itself.

class Teacher:
    def __init__(self,name,age ):
        self.name = name
        self.age = age
        #print(self)
        #print(" iam the new class teacher ")

z22 = Teacher("vikas",26)
print(z22.age)
#del z22.name # it will delete the name attribute
print(z22.name) 

##############################################

# Private(like) attributes and methods:
# conceptual attributes and methods are meant to be used only within the class
# and are not accesiblle from outside the class.

class Bank:
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd # private attribute

    def reset_pwd(self):
        print(self.__pwd)  # calling inside a class method  

a = Bank("vikas",12233)  
print(a.name)
print(a.reset_pwd())

# private method 
print('private method')
class Person:
    __nmae = "annaconda"

    def __hello(self): # private method
        print("hello world.")
    def welcome(self): 
        self.__hello() # private method caling inside a class

p1 =Person()  
print(p1.welcome())   



##################################

# inheritance:
# when one class(child/derived) derives the properties and methods
# of another class(parent/base)

#example:

# class Car:

# class Toyota(Car): 

# inheritance example
print("inheritance example.")

class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota_car(Car):
    def __init__(self,name):
        self.name = name 

car1 = Toyota_car("fortuner")        
print(car1.name)
print(car1.start())

# there are three types of inheritance
# single inheritance
#  multilevel inheritance         
# multiple inheritance

print("multiple inheritance.")

class A:
    var_a = 'welcome to the class A.'
class B:
    var_b ="welcome to the class B."    
class C(A,B):
    var_c = " welcome to the class C"    
    
c1 = C()

print(c1.var_a)
print(c1.var_b)
print(c1.var_c)

# super method:
# super() method is used to aacess methods of the parent class.

print("super method")

print("inheritance example.")

class Car:
    def __init__(self,type):
        self.type = type 

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota_car(Car):
    def __init__(self,name,type):
        self.name = name 
        super().__init__(type)    # accessing class method by super method

car2 = Toyota_car("prius",'electric')
print(car2.type)

# class method:
# A class method is bound to the class and receives the class as an implicit 
# first argument.

# non-static method can't aacess or modify class state and 
#generally for utility.
print("class method")
class Person:
    name = "annynomus"
    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("vk")
print(p1.name)
print(Person.name)        
        
# property:
#we use @property decorator on any method in the class to use 
# the method as a property.
print("property")
class Students:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def per(self):
        return str((self.a+self.b+self.c)/3) + "%"
    
st =  Students(88,89,90)
print(st.per)

st.c = 99
print(st.per)


# polymorphism: operator overloading
# when the same operator is allowed to have different meaning according 
# to the context.
print("polymorphism")
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i",+self.img,'j')

    def __add__(self,num2): # dunder function
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)     

num1 = Complex (7,9)
num1.shownumber()     
num2 = Complex (10,11)
num2.shownumber()     

num3 = num1+num2
num3.shownumber()
print(num3)

