#How would you write a Python program that checks if a given number is divisible by both 2 and 3, but not by 6? Use if, elif, and else statements to handle this scenario.

num=input("Enter a num : ")
if num%2==0 and num%3==0:
    if num%6!=0:
        print("The number is divisible by both 2 and 3, but not by 6")
    else:
        print("The number is divisible by both 2 and 3, but also by 6")
else:
    print("The is not divisible by 2,3 and 6")    


