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
'''
Wizard Duel
Let's add some more features to our Wizard class and have ourselves a Wizard duel.

Assignment
Add the following methods to the Wizard class.

get_fireballed
This method takes no inputs. First, it removes 30 health from the class instance and prints {} is hit by a fireball where {} is the name of the wizard. Then, if the wizard's health is 0 or less, it prints {} is dead.

drink_mana_potion
This method takes no inputs. It prints {} drinks a mana potion where {} is the name of the wizard, then it adds 40 to the current mana value of the wizard.
'''

class Wizard:
    def get_fireballed(self):
        self.__health -= 30
        print(f"{self.name} is hit by a fireball")
        if self.__health <= 0:
            print(f"{self.name} is dead")
    
    def drink_mana_potion(self):
        print(f"{self.name} drinks a mana potion")
        self.__mana += 40
            

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health


def main():
    merlin = Wizard("Merlin")
    print_status(merlin)
    merlin.drink_mana_potion()
    print_status(merlin)

    madame_mim = Wizard("Madame Mim")
    print_status(madame_mim)
    madame_mim.get_fireballed()
    print_status(madame_mim)
    madame_mim.get_fireballed()
    print_status(madame_mim)
    madame_mim.get_fireballed()
    print_status(madame_mim)


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()

'''
Wizard Duel
Let's give our wizards the ability to launch fireballs at each other.

Assignment
Complete the cast_fireball method.

Casting a fireball costs 20 mana
If the wizard doesn't have enough mana, raise the exception {} cannot cast fireball
Otherwise, {1} casts fireball at {2} where {1} is the caster's name and {2} is the target's name, then make sure the target is "fireballed"
'''
class Wizard:
    def cast_fireball(self, target):
        if self.__mana < 20:
            raise Exception(f"{self.name} cannot cast fireball")
        print(f"{self.name} casts fireball at {target.name}")
        self.__mana -= 20
        target.get_fireballed()

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        print(f"{self.name} is hit by a fireball")
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        print(f"{self.name} drinks a mana potion")
        self.__mana += 40


def main():
    merlin = Wizard("Merlin")
    madame_mim = Wizard("Madame Mim")

    while madame_mim.get_health() > 0:
        if merlin.get_mana() < 10:
            merlin.drink_mana_potion()

        try:
            print_status(merlin)
            print_status(madame_mim)
            merlin.cast_fireball(madame_mim)
        except Exception as e:
            print(e)


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()
'''
Encapsulation Does Not Make Systems More Secure
As we talked about earlier, encapsulation is the practice of hiding some code complexity inside a "black box" so that other developers working with the code don't have to worry about it. Adding encapsulation to our programs through "public" and "private" members makes our code easier to work with. It makes it "cleaner". To be clear, it doesn't make the code more secure in a cryptographic or cyber-security sense. That's a point I was personally confused about when I was first learning about private and public class members.

Encapsulation in Python
Python is a very dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards that languages like Go does. That's why encapsulation in Python is achieved by convention rather than by force.

Prefixing methods and properties with a double underscore is just a strong suggestion to the users of your class that they shouldn't be touching that stuff. If a developer wanted to break convention, there are ways to get around the double underscore rule.
https://stackoverflow.com/questions/3385317/private-variables-and-methods-in-python
'''