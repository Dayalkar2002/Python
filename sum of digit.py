str="143"
sum=0
for i in str:
    sum=sum+int(i)
print(sum)

                       
#recursive 
def sum(n):
    if n<10:
        return n 
    else:
        return n%10+sum(n//10)
print(sum(543))

#using while loop
def summ(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
print(summ(543))    