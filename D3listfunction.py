#add the element 100 to the end of the list.
num=[10,20,30,40,50,60,70,80,90]
num.append(100)
print(num)


#Insert the element 50 at index 2.
numbers=[10,20,30,40,50,60,70,80,90]
numbers.insert(2,50)
print(numbers)

#Remove the first occurrence of the element 30.
elements=[10,20,30,40,50,30,70,30,90,100]
elements.remove(30)
print(elements)

#sort the list in descending order.
sort=[10,20,30,40,50,60,70,80,90]
sort.reverse()
print(sort)

#List Method:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# sample input list:
list=[10,20,30,50,40]
# list.clear()
#print(list)

list.copy()
print(list)

list.extend([20,30,40])
print(list)

l=list.count(40)
print(l)

d=list.index(30)
print(d)

f=list.pop(1)
print(f)

list.remove(50)
print(list)

list.sort()
print(list)




alpha=["apple" , "cherry" , "banana"]
a=alpha.count("cherry")
print(a)


