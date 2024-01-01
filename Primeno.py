# # Prime number
# user_input=int(input("Enter the Number: "))
# if user_input<=1:
#     print(user_input,"Not a Prime Number")  
# else:
#     if user_input==2:
#         print(user_input,"is a Prime Number")
#     else:
#         i=2
#         while(i<user_input):
#              if(user_input%i==0):
#                   y=0
#                   break
#              else:
#                   y=1
#              i+=1
# if(y==1):
#     print(user_input,"is a Prime Number")
# else:
#     print(user_input,"not a Prime Number")


user_input=int(input("Enter the Number: "))

def pri(user_input):
    if user_input<=1:
        return False
    else:
        for i in range(2,user_input):
            if user_input%i==0:
                return False
        
        return True

if pri(user_input)== True:
    print(f"{user_input} is a prime number")
else:
    print(f"{user_input} is not a prime number")

