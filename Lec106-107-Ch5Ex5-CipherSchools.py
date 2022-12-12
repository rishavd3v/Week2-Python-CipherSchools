# common elements finder function 
# define a function which take 2 list as input and return a list which containscommon elements of both lists

# example
# input ----> [1,2,5,8],[1,2,7,6]
# output ----> [1,2]

# solutions

def common_elements(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

l1 = [1,2,5,8]
l2 = [1,2,7,6]
print(common_elements(l1,l2))