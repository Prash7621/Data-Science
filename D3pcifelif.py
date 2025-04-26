# Write a program that checks if a given number exists in a list.

# If the number exists, print "Number found".
# If it does not exist, print "Number not found".

my_list=[1,2,3,4,5]
number=3
if number in my_list:
    print("Number found")
else:
    print("Number is not found")


# Write a program to check if a given key exists in a dictionary:

# If the key exists, print "Key exists".
# If the key does not exist, print "Key not found".
my_dict={"name":"John","age":30,"city":"New York"}
key="age"
if key in my_dict:
    print("Key exists")
else:
    print("Key not found")

# write a program that checks if a specific element exists in a set:

# If it exists, print "Element found".
# If not, print "Element not found".
my_set={1,2,3,4,5}
element=5
if element in my_set:
    print("Element found")
else:
    print("Element not found")

# Write a program that compares two lists and prints:

# "Lists are equal" if they are identical.
# "Lists are not equal" otherwise.
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
if list1==list2:
    print("lists are equal")
else:
    print("List are not equal")


# Write a program that checks the length of a tuple:

# If the tuple has 3 elements, print "Length is 3".
# If it has more than 3, print "Length is greater than 3".
# Otherwise, print "Length is less than 3".
my_tuple=(1,2,3,4)
if len(my_tuple)==3:
    print("Length of tuple is equal to 3")
elif len(my_tuple)>3:
    print("Length of tuple is more then 3")
else:
    print("Length of tuple is less than 3")



# Dictionary Value Check:
# You are given a dictionary. Write a program that checks if a certain value exists:

# If it exists, print "Value found".
# If not, print "Value not found".
dict={"Name" : "Prashant","age" : 19}
value="Prashant"
if value in dict.values():  
    print("value found")
else:
    print("value not found")


# Write a program to perform the following operations on two sets:

# If the sets are disjoint, print "Sets are disjoint".
# If they have elements in common, print "Sets have common elements".
set1={1,2,3,4,5}
set2={4,5,6,7,8}
if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("Sets have common elements")


# Write a program that finds the maximum and minimum values in a list:

# If the maximum value is greater than 10, print "Max is large".
# If the minimum value is less than 5, print "Min is small".
# Otherwise, print "Values are normal".
list= [2, 8, 15, 4]
if len(list) > 0:
    max_val=max(list)
    min_val=min(list)   
    if max_val>10:
        print("Max is large")
    if min_val<5:
        print("Min is small")
    if max_val <=10 and min_val>=5:
        print("Values are normal")
else:
    print("The list is empty")
        


