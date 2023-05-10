# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryan'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for name in some_list:
        for key, value in name.items():
            print(key, '-', value, end=', ')
        print()


iterateDictionary(students)

# Get Values From a List of Dictionaries
studentsName = [
    {'first_name': 'Micheal', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first-name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key_name, some_list):
    for name in some_list:
        print(name.get(key_name))


iterateDictionary2('first_name', studentsName)
iterateDictionary2('last_name', studentsName)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key_name in some_dict:
        print(f"{len(some_dict[key_name])} {key_name.upper()}")
        for value in some_dict[key_name]:
            print(value)
        print()

printInfo(dojo)
