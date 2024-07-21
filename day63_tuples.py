# tuples
# tuples are the data types made of collection of items.
# the  tuples are represented by paranthesis ()
# tuples are same as list but tuples are inmutable (we cannot change )
# tuple are used because it uses less memory as compared to list 

tuple_ex = (1) # if we passing one element without coma it will act a integer
print(type(tuple_ex))

tuple_ex_2 = (1,) # it is a tuple
print(type(tuple_ex_2))

tuple_1 = (1,2,3,1.22,3.34,33333)
tuple_2 =("name","mango","vikas",1,2,True,False)
tuple_3 = (1,2,23,[22,33,45,43,29])

print(tuple_1)
print(tuple_2)
print(tuple_3)

# by using tuple function we can create tuple

tuple_a =tuple([1,2,3])
tuple_b =tuple("vikas")

print(type(tuple_a),tuple_a)
print(tuple_b)

# when we use dictionary to convert tuple the only key will be returned

dic_tuple = tuple({'vikas':'name',1:2,1.33:112})
print(dic_tuple) # only keys will be returned.

# tuplles can be accesed by using indexing 
print("tuples by using indexing.")
a= (1,2,3,4,5,6,7,8,9,10)
print(a[4])

# slicing in tuple is same as in the list 
print("slicing.")
b= (1,2,3,4,5,6,7,8,9,10)
print(b[1:])
print(b[:3])
print(b[2:6])
print(b[1:8:3])

# immutability of tuple 
# tuple are immutable we cannot change it 

# i = (1,2,3,4,5,6,7,8,9,10) 
# i[1] = 199
# print(i) # it will thros a error 

# chceking which is consuming more memory 
a = (1,2,3,7,8,6)
b =[1,2,3,3,5,5]

print(a.__sizeof__())
print(b.__sizeof__())

# tuples in a dictinory 

d = {("named","karam"):"vikas kumar",
     ("qyuwiik","ahsjskkd"):"ego"}
print(d)











