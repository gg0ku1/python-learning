

# multiple inheritance = inherit from more than one parent class
# c(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#C(B) <- B(A) <- A

class animal(): 
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")


class prey(animal): 
    def flee(self):
        print("this animal is fleeing")

class predator(animal): 
    def hunt(self):
        print("this animal is hunting")

class rabbit(prey):  #multilevel - parent - prey, grandparent - animal
    pass

class hawk(predator): #multilevel - parent - predator, grandparent - animal
    pass

class fish(prey, predator): #multiple inheritance 
    pass


rabbit1 = rabbit()
fish1 = fish()
hawk1 = hawk()

rabbit1.eat()
rabbit1.flee()
hawk1.hunt()
fish1.flee()
fish1.hunt()
