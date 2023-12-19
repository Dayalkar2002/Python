import string
user_input=input("enter the Value").lower()
x=set(user_input)
x.remove(" ")
print(user_input==set(string.ascii_lowercase))
print(string.ascii_lowercase)
