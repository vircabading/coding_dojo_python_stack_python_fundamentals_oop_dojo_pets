# //////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > OOP: Dojo Pets
# By: Virgilio D. Cabading Jr   Created: October 27, 2021
# //////////////////////////////////////////////////////////

import utl

# //// CLASSES /////////////////////////////////////////////

#  **** Pet Class ******************************************
class Pet:
    # implement __init__( name="toto" , type="dog" , tricks=["roll over", "play dead"] ):
    def __init__(self, name="toto" , type="dog" , tricks=["roll over", "play dead"]) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 50

    # sleep() - increases the pets energy by 25
    def sleep(self):
        pass

    # eat() - increases the pet's energy by 5 & health by 10
    def ear(self):
        pass

    # play() - increases the pet's health by 5
    def play(self):
        pass

    # noise() - prints out the pet's sound
    def noise(self):
        pass

    # print pet stats
    def info(self):
        utl.print_desc_center("Pet Info")
        print(F"Pet Name: {self.name} :: Type : {self.type} :: Tricks : {self.tricks} :: Health : {self.health} :: Energy : {self.energy}")