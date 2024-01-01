# class Vechile:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#         print('student info saved')

#     def show(self):
#         print(f'the model name is {self.model}')
#         print(f'the vechile name is {self.name}')


# car=Vechile('maruti',800)    
# car.show()    
# print()

#================Prime Number using Class  single inheritance ==================================

user_input=int(input("Enter the Number to check:- "))
class PrimeNo:
    def __init__(self,user_input):
        self.user_input=user_input
        print('Number Saved')

class Check(PrimeNo):
    def pri(self):
        if self.user_input<=1:
            return 'enter valid number'
        else:
            for i in range(2,self.user_input):
                if i%2==0:
                    return f'{self.user_input} is not a prime number'
                
            return f'{self.user_input} is a prime number'    
        
prime_Value=Check(user_input)
prime_Value.pri()  
print(prime_Value.pri())      

#========================Fcatorial using single iheritance===============

