# last exercise

# function 
# [1,2,3 [1,2], [3,4]] , input 
# 2
# type()

# solutions

def sub_list(l):
    count = 0
    for i in l:
        if(type(i)==list):
            count += 1
    return count

numbers = [1,2,3, [1,2], [3,4]]
print(sub_list(numbers))