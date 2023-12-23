class Factorial:
    def __init__(self,number):
        self.number=number

    def fact(self,fact=1):
        for i in range(1,self.number+1):
             fact=fact*i
        print(fact)

fact_num=Factorial(5)
fact_num.fact()        
        