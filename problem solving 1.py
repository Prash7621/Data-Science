# Write a program to display a person's name , age , and address in three differents lines.
name = "John"
age=23
address="654 lake street"
print(name)
print(age)
print(address)


# Write a program to swap two variables.
# method 1
a=23
b=12
temp=a
print(temp)
a=b
print(a)
b=temp
print(b)
print("value of a is : ",a)
print("value of b is : ",b)


# method 2
x=30
y=40

# left,right = right,left
x,y = x,y
print(y)
print(x)


# write a program to convert to float into integer.
x=12.4
print(x)
print(type(x))

x=int(x)
print(type(x))
print(x)


# write a program to take details from a student for ID-Card and then print it in different lines.
print("Students Identity Card")
name=input("enter the name of the student : ")
grade=input("enter the grade of the student : ")
age=int(input("enter the age of the stuent : "))
email=input("enter the email of the student : ")
ph_no=input("enter the phone number of the student : ")
print("name : " ,name)
print("grade : " ,grade)
print("age : " ,age)
print("email :" ,email)
print("ph_no : " ,ph_no)

# write a program to take an user input as integer then convert it to float.

num=int(input("enter the number : "))
print(num)
print(type(num))
num=float(num)
print("after conversion",a)
print(num)
