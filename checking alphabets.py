import string
user_input=input("enter the Value").lower()
user_input.replace(" ",'')
x=set(user_input)
print(x==set(string.ascii_lowercase))
print(string.ascii_lowercase)
