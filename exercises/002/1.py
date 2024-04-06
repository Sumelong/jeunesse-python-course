# RECAP

# Let's start with a quick recap:

# Variables are simply data connected to a name, like:

variable_name = "How many days have you been practicing Python?"

# An important sidenote: all the lines starting with a hashtag (#) are comments, they are a guide, helping you understand the code.

# We can assign different data TYPES to a variable

# What data types exist again?
# In python we have a lot of data types: booleans, int, float, str, list, tuple, dict are the ones we'll cover for now.
# Let's look at them in detail!

# Booleans are simply True and False statements

a_boolean = False

a_more_positive_boolean = True

# In Python if we talk about numbers we differentiate between integers (int) and floats (and complex numbers but we
# won't use these today). Integers don't have a decimal (e.g. the numbers 1, 10, and 125 are integers) while floats
# can theoretically hold an infinite amount of decimals (e.g. 3.114159)

# Here's an example of an int
an_integer = 1

# ...and here's a float:
a_float = 1.0001

# In Python you can print output to the console, you do this like so:
print(variable_name)

# Run the programm and watch what happens!

# Another data type are string (short 'str'), we use them to store text like so:

a_string = "Hey mum!"

# We also have lists, they store a list (duh) of data types and are denoted by square brackets '[]':

a_list = ["hey I am a string", 5, 3.14, (), [1, 0]]

# Looks a bit confusing? In Python you can store every data type in a list, even another list.

# you can add elements to a list trough the .append method:

a_list.append("I am a new item") # this will add the string to the previously created list

# We can access list items by index like so:

first_item_of_a_list = a_list[0]

# important! index' start at 0, so the 1st item we get by index 0 the second by index 1, ...

# To get the last item access the list from behind:

last_item_of_a_list = a_list[-1] 

# This is confusing at first, index' start at 0 but the last item is -1. What?! Because in maths 0 and -0 is equivalent we have not other choice. Better get used to it :D

# Now tuples:

a_tuple = (0, 1) 

# tuples are pretty similar to lists but you can't add elements to them (in fancy terms, they are immutable).
# You denote a tuple with round or normal brackets '()'
# This makes them more efficient. We don't use tuples super often but you should know them!

# The last data type for today is a dict, short for dictionary. They are super cool and we use them a lot for complex data storage:

a_dict = {
    "name": "vanya",
    "age": 22,
    "birthday": "07-07-2001",
    "nationality": "swiss",
}


# We talked about the if-elif-else construct, here it is again:

if a_boolean == True:
    # Do this!
    pass # we haven't seen 'pass' before, 'pass' simply says: 'go ahead!'
elif a_more_positive_boolean == True:
    # Else do this :)
    pass
else:
    # If both the if and else if condition fail we do this
    pass

# Then we have loops:
# Let's start with for loops:

for i in a_list:
    print(i)

# The above loop is going trough (or looping over) every element in our list and printing it to the console. We will use a lot of for loops :)
    
# But there are also 'while' loops, they loop until their condition is not true anymore:
    
condition_that_needs_to_be_true = True
while condition_that_needs_to_be_true:
    condition_that_needs_to_be_true = False

# The above while loop will run once and set the condition to False
    
# This code is all simple but sometimes we'll run into problems, this is why we need an error handling construct like try-except-else-finally:
    
try:
    # try some code
    pass
except:
    # if the code in the try block fails run this
    pass
else:
    # define a block of code to be executed if no errors were raised
    pass
finally:
    # Run this code no matter what happens previously
    pass

# And at last: operators
    
addition = 1 + 1 # You can add numbers

difference = 2 -1 # difference

multiplication = 1 * 5

division = 10 / 2

exponentiation = 2 ** 5

modulo = 5 % 3 # The modulo operator gives you the remainder of a division. You divide 5 by 3, the result is 1 and the remainder is 2

# That's it for the recap! On to the actual exercise! :)
