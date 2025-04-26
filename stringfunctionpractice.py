# String Functions
# 1.Write a Python program to reverse a given string.
# 2.Check whether a given string is a palindrome.
# 3.Count the occurrences of a substring in a given string.
# 4.Convert a string to uppercase and lowercase using string methods.
# 5.Write a program to find the first occurrence of a word in a given string.

r="Silver Oak University"
# 1.Reverse a given string
print(r[::-1])


p="Ahmedabad"
# 2.Check whether a given string is a palindrome
def is_palindrome(p):
    return p == p[::1]
print(is_palindrome(p))


str="Silver Oak University"
c=str.count("e")
print(c)


str2="SIlvER OaK uNiverSity"
u=str.upper(str2)
print(u)
l=str.casefold(str2)
print(l)



input_string = input("Enter the string: ")
word_to_find = input("Enter the word to find: ")

index = input_string.find(word_to_find)

if index != -1:
    print(f"The word '{word_to_find}' is first found at index {index}.")
else:
    print(f"The word '{word_to_find}' was not found in the string.")      





