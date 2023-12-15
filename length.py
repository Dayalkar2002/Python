# 1.length of character
s="manish"
print("the length is",len(s))

# 2.
x=input("enter any name :")
i=int(input("enter the index :"))
if len(x)==0:
    print('string is empty')
else:
    if(i<len(x)):
        print(x[i])
    else:
        print("i out of range")        
    

# 3.
x=input("enter the a name :")
if len(x)<6:
    print("blank output")
else:
    y=x[0:2]+x[-2:]  
    print(y)

# 4.reversed version
s="manish"[::-1]
print(s)

#5.
s="manish"[1::2]
if len(s)<1:
    print("intact")
else:
    print(s)    
    