
# define a basic function
def func1(): #this is how a function is defined
    print("this is func1")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " > ", arg2)

# function that returns a value
def func3(c):
    return c*c*c

# function with default value for an argument
def func4(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multiArgs( * args):
    result = 0
    for b in args:
        result = result + b
    return result

func1()
print(func1)
print(func1())

func2(10,20)
print(func2(10,20))

print(func3(3))
print(func4(2))

print(func4(2,4))
print(func4( x = 4, num = 2)) #py doesn't mind the re-order

print(multiArgs(4,5,10,4))
print(multiArgs(10,4,5, 9))