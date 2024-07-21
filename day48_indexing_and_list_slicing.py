# acessing element by indexing.
# indexing in python starts from 0 to n

indexing_example = ['vikas','anudeep','kamal'] 

print(indexing_example[0])
print(indexing_example[0][0])

list_in_another_list =[[1,2,3],[2,4,4],[7,8,9]]

print(list_in_another_list[2][1])

#negative indexes
print("negative indexes.")

negative_indesing =[9,7,3,4,6,4]
print(negative_indesing[-1])
print(negative_indesing[-2])
print(negative_indesing[-3])
print(negative_indesing[-4])
print(negative_indesing[-5])
print(negative_indesing[-6])

print("mixed_list")

mixed_list = [False,True,3.12,5.88,"my name is harry singh."]
print(mixed_list[1]+mixed_list[2])
print(mixed_list[1]+mixed_list[2])
print(mixed_list[4]+'i hate you')

# lsit slicing
# list slicing is used when we want a specific portion of a list.

list_slicing =[12,23,34,47,89,88,23,55] 

print(list_slicing[:4])
print(list_slicing[3:6])
print(list_slicing[4:])

# reassigning a list item.

print("reassigning  list item ")

list_r = [1,2,3,4,5,'assigning','values',99,33,44]
print(list_r)
list_r[0] = 5666
print(list_r)

# reassigning value by list.
print('reassigning value by list.')
list_r[:3] =[11,222,333]
print(list_r)








