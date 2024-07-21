# print("hello worl")
# four pillar of oops
#1. Abstarction
#2. Encapsulation
#3. inheritance 
#4. polymorphism  
#oops(object oriented programming)

# to map real world scenarios , we started using obejcts in code this
# is called oops 

# class and object:

# class:
# class is a blueprint for creating objects.

# creating a 
# class name always starts with capital letter in this Student class
class Student:
    name = 'vikas kumar'

#object:
# object is a instance of a class.        
# creating a object(instance)
s1 = Student()
print(s1) # checking the instance of a class
print(s1.name)         

# ex_2
class Car:
    brand = "benz"
    colour = "blue"

a1 = Car()
print(a1)
print(a1.brand)
print(a1.colour)

# constructor or __init__ Function
# All classes have a function called __init__(), which is always excecuted 
# when the object  is being excecuted.
# if we are not creating constructor  manually python will create 
# constructor automatically.
#note:
# the self parameter is a reference to the current instance of the class , and is used 
# to access variables that belongs to the class.
print("constructor example ............")
class Teacher:
    def __init__(self):
        print(self)
        print(" iam the new class teacher ")

z22 = Teacher()
#print(z22)

print("constructor example_2 ............")
class Friends:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        print("adding new memeber name in a class")

f1 = Friends("vikas",99)
print(f1.name,f1.marks)

f2 = Friends("kumar",98)
print(f2.name,f2.marks)


print("example_3 constructor.")

#print("constructor example_2 ............")
class Constructor_ex3:
    # default constructor
    def __init__(self):
         print("adding new memeber name in a class")
    # parameterized constructors
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        print("adding new memeber name in a class_2")

s22 = Constructor_ex3("vikas",99)
print(s22.name,s22.marks)        

# Atrributes:
# there are two types of attriutes
#1.class and 
#2. instance attributes
#class.att (calss attribute is same for all the class) 
#obj.att (object may varies it is not same for every obbject)
# obj att > class att precedence

print("class and object attribute")
class Attribut_ex:
    collge_name = "jntuh college " #class attribute
    def __init__(self,name,marks):
        self.name = name # object attribute 
        self.marks = marks
        print("adding new memeber name in a class_2")

ex = Attribut_ex("vikas",99)
print(ex.name,ex.marks,ex.collge_name)

print("class attribute is ",Attribut_ex.collge_name)

# methods:
# methods are functions that belong to object.

print('method_example')
class Method_example:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
        

m_ex = Method_example("vikas",999)        
m_ex.welcome()  
# print(m_ex.name)
print(m_ex.get_marks())

######################################################

print("code practice")

class Practice:
    def __init__(self,name,marks): 
        self.name = name
        self.marks = marks
    def average(self):
        #return self.marks/3
        sum = 0
        for var in self.marks:
            sum +=var
        print(sum/3)    
# avg = Practice("vikas",33)
# print(avg.average())

avg_2 = Practice("vikas",[10,10,10])
avg_2.average()



# static method:
# methods that don't use the self parameter(work at class level) 
# note:
# decorators allow us to wrap another function in order to extend the behaviour 
# of the wrapped function , without permanently modifying it.

print("staatic method.")

class Static_method:
    def __init__(self,name,no):
        self.name = name
        self.no = no
    @staticmethod # decorator
    def hello():
        print("welcome.")     
        

vars = Static_method("vikas",99)    
print(vars.name)    
vars.hello()


# abstraction:
# Hiding the implementation details of a class and only showing the essential 
# features to the user.

#encapsulation:
# wrapping data and function into a single unit (object)




