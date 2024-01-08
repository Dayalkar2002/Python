num=int(input("enter the number: "))
lenh=len(str(num))
Sum=0
tem_num=num
while tem_num>0:
    digit=tem_num%10
    Sum+=digit**lenh
    tem_num//=10       
if num == Sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

