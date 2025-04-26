#title()
#istrip()
#isalnum()
#isalpha()
#isnumeric()

str=input("Enter your name : ")
s=str.title()
print(s)

str2=input("Enter your college name :     ")
s2=str2.strip()
print(s2)

str3=input("Enter your city : ")
str3=str.isalnum()
print(str3)

str4=input("Enter your state : ")
a=str4.isalpha()
if str4.isalpha():
    print(a)
else:
    print("Invalid input")



str5=input("Enter a num: ")
t=str5.isnumeric()
if str5.isnumeric():
    print(t)
else:
    print("Please enter numeric value!")



