import string

tup1 = (1,2,3,4,5)
tup2 = (5,)

print(tup1+tup2)

# UNPACKING
tup = ('xx', 'yy', 'zz')
(x,y,z) = tup
print(z)

# Convert the tuple into a list to be able to change it:
tup1 = (4, 6, 2, 8, 3, 1)
list1 = list(tup1)
list1.insert(2, 100)
print(tuple(list1))


# Tuple naar string
tup = ('a', 'b', 'c')
str = ''.join(tup)
print(str)

# List naar tuple
List3 = [5, 10, 7]
print(tuple(List3))

# Lijst met tuples joinen

FL = [(1, 2), (3, 4), (8, 9)]
FL = list(zip(FL[0], FL[1], FL[2]))
print("F: ", FL)

# van lijst met tuples naar dict

L1 = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2),("y", 3) ]
L1.append(tuple("z1"))

#Sorteren dict

D = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}

D = sorted(D.items())

for item in D:
    print(item[0], "->", item[1])

# Dict alleen unieke waardes
D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5}

unique = {}

for key,value in D.items():
    if value not in unique.values():
        unique[key] = value

print(unique)

# Dict alleen unieke waarden via set

print ("--------")
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

S = set()

for i in L:
    for key, value in i.items():
        S.add(value)

print(S)


# Waarden bij elkaar optellen met counter
from collections import Counter

L = [{'a': 1, 'b': 2, 'c': 3}, {'a': 5, 'b': 4, 'c': 2}]

print(Counter(L[0]) + Counter(L[1]))


# Twee lijsten samenvoegen met zip
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

D = dict(zip(keys, values))

print(D)


# Doorsnede van twee sets
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}

print(s1.intersection(s2))

# Symetrisch verschil twee sets
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}

print(s1.symmetric_difference(s2))

# Check of er items in de set staan
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
S = set(L)

print( 15 and 11 in S )


# COMPREHENSION
# Capatalize

capitalize = [ letter.capitalize() for letter in ["j", "i", "m"] ]
print(capitalize)

# Add when letter is uppercase
res = []
onlyupper = [ res.append(letter) for letter in ["J", "i", "m"] if letter.isupper()]
print(res)


#Functies

def unique_list(l):
    res = []
    for letter in l:
        if letter not in res:
            res.append(letter)
    return res

print(unique_list([1,2,3,3,3,3,4,5]))


def even_numbers(l):
    res = []
    for number in l:
        if number % 2 == 0:
            res.append(number)
    return res

print(even_numbers( [1, 2, 3, 4, 5, 6, 7, 8, 9] ))




def is_pangram(str):
    alfabet = list(string.ascii_lowercase)
    for letter in str.lower():
        if letter in alfabet:
            alfabet.remove(letter)

    if len(alfabet) == 0:
        return True
    else:
        return False

print(is_pangram( "Filmquiz bracht knappe ex-yogi van de wijs"))


#Sorteer dict


def sort_dict(d):
    res = []
    for key, value in d.items():
        res.append((key, value))
    return sorted(res)

d = {'ed': 5, 'carl':3, 'alan':1, 'bob':2, 'dan':4}
print(sort_dict(d))