import string
user_input=input("enter the Value")
x=set(user_input.lower())
x.remove(" ")
print(user_input==set(string.ascii_lowercase))
print(string.ascii_lowercase)
