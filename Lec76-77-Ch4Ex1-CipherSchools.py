def greater(a,b):
    if a>b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
bigger = greater(a,b)
print(f"{bigger} is greater")