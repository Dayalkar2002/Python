# Greater Between Two Number

x=int(input("Enter First Number :"))
y=int(input("Enter Second Number :"))
if(x>y):
    print(x,"is greater")
else:
    print(y,"is greater") 

#Greater Between Three Number

x=int(input("Enter First Number :"))
y=int(input("Enter Second Number :"))
z=int(input("Enter the thitd number :"))
if(x>y and x>z):
    print(x,"is greater")
elif(y>z and y>x):
    print(y,"is greater")
else:
    print("z is greater")       

