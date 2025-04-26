# Write a Python program to find all the numbers divisible by 3 in a given list. Use a user-defined function to check divisibility, and use a for loop or list comprehension to collect the results.

# Input: [10, 15, 20, 21, 30, 33, 50, 60]
# Output: [15, 21, 30, 33, 60]
# def check_divisibility(num):
#     return num % 3 == 0

# list= [10, 15, 20, 21, 30, 33, 50, 60]
# number =  [num for num in list if check_divisibility(num)]


# print("Number is divisible by 3 : " ,number)
        



# check_divisibility = lambda num : num%3==0
# list=[10, 15, 20, 21, 30, 33, 50, 60]  
# number =  [num for num in list if check_divisibility(num)]

# print(number)


# Write a Python program to find all numbers greater than 50 in a given list. Use a lambda function within a user-defined function to check if a number is greater than 50. Use a for loop or list comprehension to collect the results.
# Input: [10, 55, 60, 45, 90, 20, 100, 40]
# def myfunc(num):
#     return lambda num : num > 50
# list=[10, 55, 60, 45, 90, 20,100,40]
# mydoubler=myfunc(list)
# # number = [num for num in list if mydoubler(list)]
# print(mydoubler(list))

# def my_function(num): 
#     return lambda num : num>50
# list=[10, 15, 20, 21, 30, 33, 50, 60]
# mydoubler=my_function(list)  
# number =  [num for num in list if mydoubler(num)]

# print(number)



#You are managing a small library system and have a list of books. Each book is represented by a dictionary with the following information: title, author, and year_published. Write a Python program to filter out books that were published before the year 2000. You should use a user-defined function to check the publication year and a for loop to iterate through the list of books.

# books = [
#     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
#     {"title": "1984", "author": "George Orwell", "year_published": 1949},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1925},
#     {"title": "The Road", "author": "Cormac McCarthy", "year_published": 2006},
#     {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year_published": 1951},
# ]

def func(book):
    return  book["year_published"] >= 2000
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
    {"title": "1984", "author": "George Orwell", "year_published": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1925},
    {"title": "The Road", "author": "Cormac McCarthy", "year_published": 2006},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year_published": 1951},
]

poetry = [book for book in books if func(book)]
print(poetry)


# def func(book):
#     return book["year_published"] >= 2000
# books = [
#     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
#     {"title": "1984", "author": "George Orwell", "year_published": 1949},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1925},
#     {"title": "The Road", "author": "Cormac McCarthy", "year_published": 2006},
#     {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year_published": 1951},
# ]
# before_2000 = []
# for book in books:
#     if func(book):
#         before_2000.append(book)
# print(before_2000)