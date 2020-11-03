# 
# Example file for variables
#

# Declare a variable and initialize it
x = "Jane"
print(x)
f = 0
# re-declaring the variable works
x = 123
print(x)


# ERROR: variables of different types cannot be combined
print(" this is a str ", 123)
# print("this is a str " + 123)  //this cannot work
print(" this is a string " + str(123))

# Global vs. local variables in functions
def myFunction():
    global f
    f = "new f"
    print(f)

myFunction()
print(f)

# del f # deletes the variable definition
