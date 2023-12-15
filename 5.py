str=input("Enter the string: ")
i=int(input("Enter the index"))
if len(str)==0:
    print("Empty string")
elif(i>len(str)):
    print("index is out of range")
else:
    print('Charater at index',i,'is',str[i])
    
