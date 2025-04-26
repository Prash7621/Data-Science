try:
    f = input("Enter a file name : ")
    try:
        f = open(f,'r')
    except PermissionError:
       print("File dosen 't' exist permission")
except FileNotFoundError:
    print("File dosen 't' exist")
finally:
    print("Task Completed")




try:
    Fahrenheit=int(input("Enter temp in fahrenheit : "))
    try:
        Celsius=(Fahrenheit-32)*5/9
        print(Celsius)
    except Exception as e:
        print("An unexpected error occured")
except ValueError:
    print("Invalid input , Enter a number ")
finally:
    print("Conversion attempt finished")


     