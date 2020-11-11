a = 1
b = 2
def func():
    global b 
    b = a + b
func()
print(b)

def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)