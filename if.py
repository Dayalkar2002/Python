# 1st code
x=int(input("Plase enter x"))
y=int(input("Plase enter y"))
if(x>y):
     print("X is greater")
else:
 print("y is greater")     

# 2nd code
x=int(input("Plase enter x"))
y=int(input("Plase enter y"))
z=int(input("Plase enter z"))
if(x>y and x>z):
     print("X is greater")
elif(y>z and y>x):
 print("y is greater")
else :
 print("z is greater")
 
#3.
x=int(input("Plase enter x"))
y=int(input("Plase enter y"))
z=int(input("Plase enter z"))
w=int(input("Plase enter w"))
if(x>y and x>z and x>w):
     print(x,"is greater")
     
elif(y>z and y>w and y>x):
 print(y,"is greater")
 
elif(z>w and z>x and z>y):
 print(z,"is greater")
 
else :
 print(w,"is greater")