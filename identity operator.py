# identity operator are used to comapre the objects. not if they are equal ,  but if they are actually the same object , with the same memory location:

# 1. is  (return true if both the variables are the same object) 

x=["apple" , "banana"]
y=["apple" , "banana"]
z=x

print(x is z)  #true

print(x is y) # false

print(x == y) # true

# 2. is not  (returns true if both variables are not the same object)

x=["apple" , "banana"]
y=["apple" , "banana"]
z=x

print(x is not z)  #false ( beacuse z is the same object as x)

print(x is not y) # true  (beacuse  x is not same object as y , even if they have the same content)

print(x != y) # false


