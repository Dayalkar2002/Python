# class Calculator:
#     def add(self,a,b,c=None):
#         if c is not None:
#             return a+b+c
#         else:
#             return a*b
    
# calc=Calculator()
# result1=calc.add(2,3)
# print(result1)


#======using variable length argument========
class Calculator:
    def add (self,*args):
        return sum(args)
    
calc=Calculator()    
result1=calc.add(1,2,3)
print(result1)