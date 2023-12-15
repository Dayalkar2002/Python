str=input('enter the name: ')
length=len(str)
if (length==0 and length==1):
    print('intact')
else:
    print('characters of even string',str[1::2])    
