# scope

x = 5

def func():
    global x
    x = 6    #local variable
    return x

print(x)
print(func())
print(x)