# Write a program that adds all letters from the individual data types to form a complete alphabet in the list named 'alphabet'
# Hint: use what you learned about for loops, .append() and list/dict access trough index

a = "a"
list = ["b", "c", "d", "e", "f", "g"]
dict = {
    "one": ["h", "i", "j", "k", "l", "m", "n", "o"],
    "two": ("p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
}

alphabet = []
# append 'a' to alphabet list
alphabet.append(a)

# append all list letters to alphabet list
for letter in list:
    alphabet.append(letter)

# extract one's list
one = dict["one"]
# append one's letters to alphabet list
for letter in one:
    alphabet.append(letter)

# extract two's list
two = dict["two"]
# append two's letters to alphabet list

for letter in two:
    alphabet.append(letter)


# Don't delete this, this line will check if your exercise is correct when you run the code
assert alphabet == ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"], "Your code doesn't quite work yet, don't give up!"
