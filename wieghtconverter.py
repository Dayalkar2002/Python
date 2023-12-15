Weight=int(input("Enter the weight: "))
Unit=input("(K)kg or (L)lbs: ")
if Unit.upper()=='K':
    print('You are', Weight//0.45, 'Pounds')
else:
    print('You are', Weight*0.45, 'Kilos')
