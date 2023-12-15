#using while loop
fib_num=int(input("enter the fibonacci number: "))
n1=0
n2=1
count_start=0
if (fib_num<=0):
    print("enter number greater than 0")
else:
    while(count_start<fib_num):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count_start+=1
        

 