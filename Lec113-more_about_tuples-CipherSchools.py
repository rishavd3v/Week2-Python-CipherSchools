# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
# NOTE - You can use while loop too

# tuple with one element
nums = (1)
words = ('wordl')
# print(type(nums))
# print(type(words))

# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))


# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitaristl, guitarist2, guitarist3 = (guitarists)
# print(guitarist1)

# list inside tuples
favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it ")
print(favorites)

# min(), max, sum 
print(min(mixed))
print(max(mixed))