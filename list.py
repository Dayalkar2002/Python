#Python program that prints (as a list) the elements of listA that are not in listB as a list
l1=[1,2,3,4,5,6]
l2=[1,2]
x=[]
for i in l1:
    if i not in l2:
        x.append(i)    
print(x)

#calculate distance between two 3d points
import math
x=[4,5,6]
y=[8,9,12]
distance=((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2)**0.5
print(distance)


print(math.factorial(5))

# largest number
l=[1,2,3,4,5,6,7,8,9]
sum=l[0]
for i in l:
    if i>sum: 
       sum=i
print(sum) 

#write python program that counts the number of elements in a list with value greater than 3

count_list=[1,2,3,4,5,6,7,8,9]
entry_list=[]
for i in count_list:
    if i>3:      
      entry_list.append(i)
final=len(entry_list)  
print("total count is=",final)   

#convert nested list into plain list
nest_list=[[1,2,3],[4,5,6],[7,8,9]]
empty_list=[]
for i in nest_list:
    for j in i:
        empty_list.append(j)
print(empty_list)        
