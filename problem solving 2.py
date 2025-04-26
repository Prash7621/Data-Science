# write a program to check if a number is positive .

num = 3
if num>0:
    print("num is positive")

# write a program to check whether a number is odd or even.

num = int(input("enter a num : "))
if num % 2 == 0:
    print("num id even")
else:
    print("num is odd")

# write a program to create area calculator.
print("***** AREA CALCULATOR ******")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input("enter a number between 1-4 : "))

if choice == 1:
    side = float(input("Enter the length of one side : "))
    area = side**2
    print("The area of square is : " , area)

elif choice == 2:
    length = float(input("enter the length of rectangle : "))
    width = float(input("enter the width of the rectangle : "))
    area = length*width
    print("The area of rectangle is " , area)
elif choice == 3 :
     radius=