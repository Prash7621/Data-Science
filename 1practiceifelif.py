# Problem: Write a Python script that classifies students based on their grades. The script should ask the user for the student's grade and then determine the classification according to the following criteria:
# A grade of 90 or above is classified as "Excellent".
# A grade between 70 and 89 (inclusive) is classified as "Good".
# A grade between 50 and 69 (inclusive) is classified as "Average".
# A grade below 50 is classified as "Fail".
# Get the student's grade from user input

print("Enter your marks")
Total_marks=500
sub1=int(input("Enter your marks of sub1 : "))
sub2=int(input("Enter your marks of sub2 : "))
sub3=int(input("Enter your marks of sub3 : "))
sub4=int(input("Enter your marks of sub4 : "))
sub5=int(input("Enter your marks of sub5 : "))

Total = [sub1, sub2 , sub3 ,  sub4 , sub5]
print("Marks obtained out of",Total_marks ," : " ,sum(Total))
obtained_marks=sum(Total)

percentage = (obtained_marks/Total_marks) * 100
print("Percentage : " ,percentage)


if percentage>=90:
    print("Excellent")
elif percentage<=89 and percentage>=70:
    print("Good")
elif percentage<=69 and percentage>=50:
    print("Average")
else:
    print("You are Fail")

