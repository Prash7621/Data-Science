# List Question:
# Write a program to iterate through a list of numbers and print only the even numbers.
my_list=[1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    if num%2==0:
        print(num)
    
# Dictionary Question:
# Given a dictionary of student names and their age, iterate through the dictionary and print each student's name along with their age.
my_dict= {
     "Prashant" : 20,
     "Danish" : 21,
     "Dipak" : 22
}

for student , age in my_dict.items():
    print(f"{student} is {age} years old")



#Set Question:
#Create a set of numbers, iterate through it using a loop, and print each number.
my_set = {1,2,3,4,5,6,7,8}
for num in my_set:
    print(num)

#Tuple Question:
#Given a tuple of fruits, write a program to print each fruit's name in reverse order.
my_tuple=("apple","banana","cherry","date","elderberry")
for fruit in my_tuple:
    print(fruit[::-1])


# List Question:
# Write a program to calculate the sum of all elements in a list using a loop.
numbers=[1,2,3,4,5]
sum=0
for num in numbers:
    sum+=num
print(sum)


number=[1,2,3,4,5]
sum=0
for nums in number:
    sum += nums
    print(sum)


# Dictionary Question:
# Create a dictionary where the keys are numbers (1-5) and the values are their squares. Use a loop to construct the dictionary.
Dictionary={}
for i in range(1,6):
    Dictionary[i]=i ** 2
print(Dictionary)


# Set Question:
# Write a program to remove all odd numbers from a set of integers using a loop.

nums={1,2,3,4,5,6,7,8,9,10}
even_numbers=set()
for num in nums:
    if num % 2 == 0:
        even_numbers.add(num)
print(even_numbers)

# Tuple Question:
# Given a tuple of integers, write a program to count how many numbers are greater than a given value n.
counts=(1,2,3,4,5,6,7,8,9,10)
n=5
count=0
for num in counts:
    if num < n:
       count+=1
print(count)


# List & Set Question:
# Convert a list with duplicate elements into a set to remove duplicates, then print the set.
numbers=[1,2,2,3,4,4,5,6,6]
set_numbers=set(numbers)
print(set_numbers)


# Dictionary & Loop Question:
# Write a program to iterate through a dictionary and calculate the sum of all its values.
# Use a loop to iterate through the dictionary.
d={'a':1,'b':2,'c':3,'d':4,'e':5}
total=0
for value in d.values():
    total+=value
print(total)


