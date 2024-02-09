#factorial of number using recursive function.
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    


#basic factorial
fact_num=int(input("enter the factorial number: "))
fact=1
for i in range(1,fact_num+1):
    fact=fact*i
print(fact)


# using normal function
def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
user_input=int(input("enter the number : "))
print("The factorial of given number is",fact_num(user_input))    
