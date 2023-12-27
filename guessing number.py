
num=9
Guess_Count=0
Guess_Limit=3
while Guess_Count<Guess_Limit:
    user_input=int(input("enter the number:- "))
    if user_input==num:
        print("You are right")
        break
    else:
        print("Wrong guess!! Please try again")
        Guess_Count+=1