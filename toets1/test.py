numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)

#OUTPUT:
#{(1, 'ONE'), (2, 'TWO'), (3, 'THREE')}


result = zip(numbersList, strList, numbersTuple)
# Converting to set
resultSet = set(result)

#OUTPUT:
#{(2, 'two', 'TWO'), (1, 'one', 'ONE')}