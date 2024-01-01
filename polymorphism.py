class Species:
    def speed(self):
        pass

class Cheetah(Species):
    def speed(self):
        print('the speed of the cheetah is 100kmph')


class Lion(Species):
    def speed(self):
        print('the speed of the Lion is 40-60kmph')

class Tiger(Species):
    def speed(self):
        print('the speed of the Tiger is 80kmph')        


def speed_check(Species):
    Species.speed()        

cheetah=Cheetah() 
lion=Lion()   
tiger=Tiger()

(speed_check(lion))