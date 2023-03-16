'''
Encapsulation
Encapsulation is one of the strongest tools in your tool belt as a software engineer. As we covered in chapter one, writing code that machines understand is easy, but writing code that humans can understand is very difficult.

Encapsulation is the practice of hiding information inside a "black box" so that other developers working with the code don't have to worry about it.

encapsulation

A basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

acceleration = calc_acceleration(initial_speed, final_speed, time)
In the example above, to use the calc_acceleration function, we don't need to understand what goes on inside. That's the goal of encapsulation, it makes our lives easier as developers and helps us write cleaner code.

Encapsulation in OOP
In the context of object-oriented programming, we can practice good encapsulation by using private and public members. The idea is that if we want the users of our class to interact with something directly, we make it public. If they don't need to use a certain method or property, we make that private to keep the usage instructions for our class simple.

Encapsulation in Python
To enforce encapsulation in Python, developers prefix properties and classes that they intend to be private with a double underscore.

class Wall():
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall
        self.__height = height

    def get_height(self):
        return self.__height
In the example above, we don't want users of the Wall class to be able to change its height. We make the __height property private and expose a public get_height method so that users can still read the height of a wall without being tempted to update it. This will stop developers from being able to do something like:

# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error
Assignment
Complete the Wizard class. Its constructor should take a name as input. It should set the public name property to the given name. It should also initialize private __mana and __health properties to 45 and 65 respectively.

Create two "getter" methods. One called get_mana() and one called get_health(). They should return the current mana and health of the class instance respectively.
'''
class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name
        
    def get_mana(self):
        return self.__mana
    
    def get_health(self):
        return self.__health


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    merlin = Wizard("Merlin")
    madame_mim = Wizard("Madame Mim")

    print_status(merlin)
    print_status(madame_mim)


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()