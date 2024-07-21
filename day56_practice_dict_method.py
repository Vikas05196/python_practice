# create a variable and assign it the following dictionary:

example_dict = {"Queen": "Bohemian Rhapsody", 
                "Bee Gees": "Stayin' Alive", 
                "U2": "One", 
                "Michael Jackson": "Billie Jean", 
                "The Beatles": "Hey Jude",
                  "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

# print the length of the dictionary.
print(len(example_dict))
# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in example_dict.keys():
    print(key)
    
# print all of the values from the dictionary using the .values() method.
print(example_dict.values())
# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for ke, value in example_dict.items():
    print(ke , value)
    
# use the .get() method to check the dictionary for the key
print(example_dict.get("janagaa","the key did not find in the dictionary"))
# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

print("solutions")
# solutions 
famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
print(len(famous_songs))  # 3
for key in famous_songs.keys():  # 4
    print(key)
print(famous_songs.values())  # 5
for key, value in famous_songs.items():  # 6
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7




