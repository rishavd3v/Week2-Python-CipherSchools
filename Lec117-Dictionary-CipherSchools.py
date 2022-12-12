# dictionaries introduction 
# Why use dictionaries
# Because of limitiations of lists, lists are not enough to represent real data.


# example
user = ['Harsit', 24,['coco', 'kimi no na wa'],['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can do this but it is not a good way to do this.

# dictionaries are ordered collection of data in key : value pair.
# 
# create dictionaries 
user = {'name' : 'Rishav', 'age' : '18'}
# print(user)
# print(type(user))

# 2nd method

user1 = dict(name='Rishav', age = 18)
print(user1)


# access data from dictionaries
# Note - There is no indexing because unoe=rdered collections of data 
print(user['name'])
print(user['age'])

# which type of data a dictionary can store?
# anything!


user_info = {
    'name' : 'Rishav',
    'age' : 18,
    'fav_movies' : ['coco', 'star wars', 'intersteller'],
    'fav_tunes' : ['awakening', 'kimi no na wa'],
}

print(user_info['fav_movies'])


# Add data to empty dictionary

user_info2 = {}
user_info2['name'] = 'Rishav'
user_info2['age'] = 18

print(user_info2)