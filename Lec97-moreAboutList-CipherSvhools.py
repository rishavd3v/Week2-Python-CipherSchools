# generate list with range functions
# something more about pop method
# index method
# pass list to a function 

numbers = list(range(1,11))
print(numbers)

popped_items = numbers.pop()
print(numbers)
print(numbers.index(1,11,14))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list)