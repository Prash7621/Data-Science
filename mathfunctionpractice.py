# Math Functions
# 1.Write a Python program to calculate the square root of a number using the math module.
# 2.Find the GCD (Greatest Common Divisor) of two numbers using the math module.
# 3.Generate a random float number between 0 and 1 using the random module.
# 4.Write a program to calculate the factorial of a number.
# 5.Use math.pow() to calculate x^y , where x and y are input from user.




import math
r=math.sqrt(64)
print(r)
x=math.sqrt(int(input("Enter sqaure number : ")))
print(x)


y=math.gcd(4,6)
print(y)


import random
num=random.random()  # random.random() to generate number between 0 and 1
print("Your random number is : " , num)



import math
m=math.factorial(5)
print(m)


import math
i=float(input("enter value of x : "))
s=float(input("Enter value of y : "))
p=math.pow(i,s)
print(p)


