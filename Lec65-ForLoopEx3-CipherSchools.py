# practice for loop
# ask user name and count each character

# Rishav
# R : 1
# i = 2
# s : 3
# h : 4
# a : 5
# v : 6


name = input()
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]


