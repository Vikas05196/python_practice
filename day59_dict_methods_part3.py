# .clear()
#.copy()
# .update()

# .clear() method is used to remove the every items in a dictionary and it returns 
# a empty dictionary 
# clear() method takes a no arguments

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", 
                   "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items)
clear =fast_food_items.clear()
print(clear)

# .copy() method is used to copy the one dict variable to another dict variable 
# as it has been sahring a same refference

var_pop = {"name ":"vikas","village":"kaka",1:333}
print(var_pop)
b = var_pop.copy() #(doubt) the copy method is used to used to change the referenec of a dictionary element 

b[1] = 18889
print(var_pop)
print(b)


# .update() is used to update the value from one dictionary to another dictionary 

var_update  = {"name ":"vikas","village":"kaka",1:333}
var_upadte_2 = {"values":123}

var_update.update(var_upadte_2)
var_upadte_2 ["values"] = 888888

print(var_update)
print(var_upadte_2)

n_dict  = {"name ":"vikas","village":"kaka",1:333}
n_dict.update({}) # when we pass empty dict it does not effect anything.

print(n_dict)




