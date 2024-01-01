class Students:
    def __init__(self,name,age,id,city):
        self.name=name
        self.age=age
        self.id=id
        self.city=city
        print("Students info saved")

    def intro(self):
        print(f'The name is {self.name}') 
        print(f'The age is {self.age}')  
        print(f'The id is {self.id}') 


School=Students('manish',19,1,'Mumbai')  

