string = "Hello World."

print(string.upper())
var_b = "THIS IS A CAPITAL LETTER."
print(var_b.lower())

# .isupper() and .islower() methods. both returns a boolean value
print("VARIOUS METHODS.")
print("kkakkk".isupper())
print("kkakkk".islower())
print("kARMA".islower())



print("KARMA".islower())
print("KARMA".isupper())

print("KARMA".lower().isupper())

print("KARMA".lower().islower())


# .isalpha() => only letters
# .isalnum() => alphabet and numbers
# .isdecimal() => only numbers
# .isspace() => only spaces.
# .istitle() => only titlecase. Ex: word that starts with cpitals letters.
# Example: Happy Birthday.

print("examle.")
print("batman".isalpha())
print("batman123".isalpha())
print("batman".isalnum())
print("123batman".isalnum())
print("alnum")
print("123".isalnum())
print("123".isalnum())
print("isdecimal.")
print("123".isdecimal())
print("123.565".isdecimal())
print("# isspcae")
print("   ".isspace())
print("".isspace())
print("this is a spcae".isspace())
print("this is a spcae"[4].isspace())

print("is title.")

print("This Is A Title Case".istitle())
print("his has A Title Case".title())

# .startswith() and .endwith()
print("startswith")
print("I hate you".startswith("I"))
print("I hate you".endswith("u"))

# join => multiple strings join together.
# .join()

print("".join(["ram","rahim","junior"]))
print(" ".join(["ram","rahim","junior"]))
print(",".join(["ram","rahim","junior"]))
print(".....".join(["ram","rahim","junior"]))

# .split() => it is used to split list
print("split")
print("eggs,white,toaste".split())
print("eggs,white,toaste".split(","))
print("eggs,white,toaste".split(","))












