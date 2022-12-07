# practice for loop
# ask user a number like 1256
# calculate sum of digits

#logic
# num = 1256
# int(num[0]) ---> 1
# int(num[1]) ---> 2
# int(num[2]) ---> 5
# int(num[3]) ---> 6

total = 0
num = input()
for i in range(0,len(num)):
    total += int(num[i])
print(total)