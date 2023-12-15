s=input('enter string')
str=''
for i in s:
    str=i+ str
print(str)


#using function

def reverse_string(value):
    str=""
    for i in value:
        str=i+str
    print(str)
user_input=input("Enter the value: ")
reverse_string(user_input)        