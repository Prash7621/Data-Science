# Write a Python program that checks if a number is either divisible by 2 or divisible by 3 but not both, using if, elif, and else to display the correct message.

num=int(input("Enter a num : "))
if num%2==0 and num%3!=0:
    print("The number is divisible by 2 but not by 3")
elif num%3==0 and num%2!=0:
    print("The number is divisible by 3 but not by 2")
elif num%2==0 and num%3==0:
    print("The number is divisible by both 2 and 3")
else:
    print("The number is not divisible by both 2 and 3")