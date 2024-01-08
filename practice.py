# def reversed_string(value):
#     str=""
#     for i in value:
#         str=i+str
#     return str
# user_input=input("enter the string: ")
# print(reversed_string(user_input))
#===============================================

#write a python program that finds area of circle from the value of the diameter d
# diameter=int(input("enter the diamter: "))
# radius=diameter/2
# area_of_circle=3.14*(radius)**2
# print("the area of circle is= ",area_of_circle)
# print()

#write a python program that computes the area of a triangle from its base and height
# base=int(input("enter the base: "))
# height=int(input("enter the hieght: "))
# area_of_triangle=0.5*(base*height)
# print("the area of traingle is= ",area_of_triangle)
# print()

#write a python program that coverts degree celcius into degree farenheit
# degree_celcius=int(input("enter the degree celcius value: "))
# degree_farenheit=degree_celcius*9/5+32
# print("degree celsius=",degree_farenheit,"Farenheit")
# print()

#
# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S")) 


#sum of digits
# number=input("enter the number: ")
# sum=0
# for i in number:
#     sum=sum+int(i)
# print("sum of digits is",sum) 

#write a python program that checks if a key exists in a dictionary or not
# dream_11={"Name":"Manish","age":21,"mobile":9892590046}
# if 'Name' in dream_11.keys():
#     print("true")
# else:
#      print("False")   
# print()

#write a python program that adds a new key-value pair to a dictionary only if the key doesnt exitst already


#write a python program that merges two dictionaries and print the resulting dictionary
# dream_11={"Name":"Manish","age":21,"mobile":9892590046}
# team_11={"Sirname":"Dayalkar"}
# new_11=dream_11.update(team_11)
# print(new_11)

#nested dictionary
# dream_11={"fullname":{"Name":"Manish","sirname":"Dayalkar"},"age":21,"mobile":9892590046}
# for i in dream_11:
#      if type(dream_11[i]) is dict:
#           for j in i
               


#write a python program that checks if all values in a dictionary are equal
# my_dic={'a': 10, 'b': 10, 'c': 10, 'd': 10}
# values=my_dic.values()
# check=list(values)[0]
# for i in my_dic:
#      if my_dic[i]==check:
#           print(True)
#           break
# else:
#      print(False)
    

#write a python program that prints largest value in a dictionary     
# my_dic={'a': 110, 'b': 112, 'c': 97, 'd': 40}
# values=my_dic.values()
# print(values)
# num=my_dic['a']
# for i in values:
#        if i>num: 
#           num=i
# print(num)

#write a python program that creates a dictionary from the values contained in nested lists
# manish=[['manish',1],['sahil',2],['piyu',3]]
# new_manish=dict(manish)
# print(new_manish)



#map()

# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared= map(square, numbers)

# result = list(squared)
# # result = list(map(square,numbers))

# print(result)

# print()

# sum=0
# for i in range(1,4):
#   for j in range(1,3):
#     if i!=j:
#       sum=sum+i+j
# print(sum)      

# x=4
# y=9
# while x<y:
#   x=x+1
#   y=y-1
# print(x-y)  


# x=8
# y=9
# print(x,y)

    
      
  


    
    
        


        

    
    


