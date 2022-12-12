# function inside function 

# greater(a,b) -----> a or b 
# greater(a or b, c) -----> greatest

def greater(a,b):
    if a>b:
        return a
    else:
        return b

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

print(new_greatest(10,50,43))
