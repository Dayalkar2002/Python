# Define a lambda function 'r' that takes a single argument 'a' and returns 'a + 15'
r=lambda a:(a+15)
print(r(10))

# Reassign 'r' to a new lambda function that takes two arguments 'x' and 'y' and returns their product
r=lambda x,y:(x*y)
print(r(4,5))

#Write a Python program to create a function that takes one argument,and that argument will be multiplied with an unknown given number.

def number(n):
    return lambda x:x*n

result=number(2)
print("double the number 15 =",result(15))

#Write a Python program to sort a list of tuples using Lambda.

subject_marks=[('English',98),('Science',90),("Maths",95)]
subject_marks.sort(key=lambda x:x[0])
print(subject_marks)


