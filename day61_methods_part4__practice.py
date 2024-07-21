var_update  = {"name ":"vikas","village":"kaka",1:333}

if "lenovo" not in var_update:
    var_update["lenovo"] = "think pad"
print(var_update)

# .setdefault() is used  to find the keys that does not exist if not exist it will add the value.
# set default takes the two values one is key and another is values.
# the values remain unchanged if we  find it.

set_default  = {"name ":"vikas","village":"kaka",1:333}

set_default.setdefault(11,12121)

print(set_default)

set_default.setdefault(11,333333333333) #the values of key 11 remain unchanged 

print(set_default)

print("set defaults.")

default_var  = {"name ":"vikas","village":"kaka",1:333}

default_var.setdefault(44,88888888)

print(default_var)
