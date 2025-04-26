# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

dict={'a': 1, 'b': 2, 'c': 3}
dict.update({'d': 4})
print(dict)

dict.update({'b' : 20})
print(dict)

if dict.fromkeys({'e' : 20}):
    print( "yes , e is present in the dict")
else:
    print( " no , e is not present in the dict")