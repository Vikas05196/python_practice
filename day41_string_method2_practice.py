#.ljust() => add spaces to the left
#.rjust()  => add spaces to the right

print("hello world".rjust(15))
print("hello world".ljust(15)+"four error")

# we can add only one letter along with one argument with .ljsut and .rjust

print("hello world".rjust(18,'.'))
print("hello world".ljust(19,"*"))

# .center() is used to keep the word at the center

print("hello world".center(16))
print("hello world".center(17,':'))


# .strip() ,.lstrip(),.rstrip()

# strip removes spaces from both side ,.lstrip removes the spaces from lefft side 
# .rstrip removes the spaces from right side.
print("strips")
print("it was a great journey 1111111111")
print("it was a great journey 1111111111".strip("1"))
print("it was a great journey 1111111111".lstrip("1"))
print("it was a great journey 1111111111".rstrip("1"))

print("juice,bread,jam,kam, juice".rstrip(", juice"))
print("juice,bread,jam,kam, juice".lstrip("juice,"))
print("juice,bread,jam,kam, juice".lstrip("juice,bre"))

print("blueblueyellowblue".strip("eulb"))
print("blueblueyellowblue".strip("blue"))
print("aaaaaabbbbbbbbaaaaaa".strip("a"))

# .replace() is used to replace the word when the string found it takes 
# two arguement one is the word and the word that is to be replaced

print("hello world".replace("world","hyderabad"))
print("helloworld".replace("hello","hyderabad"))












