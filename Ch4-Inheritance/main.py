'''
Inheritance
We've made it to the Holy-grail of object-oriented programming: inheritance. Inheritance is the defining trait of object-oriented languages. Non-OOP languages like Go and Rust provide encapsulation and abstraction features as almost every language does. Inheritance on the other hand tends to be unique to class-based languages like Python, Java, and Ruby.

What is inheritance?
Inheritance allows one class (aka "the child class") to inherit the properties and methods of another class (aka "the parent class").

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

Syntax
In Python, one class can inherit from another using the following syntax.

class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
To use the constructor of the parent class, we can use Python's built-in super() method.

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)
Assignment
In Age of Dragons, all the archers in the game are humans, though not all humans are necessarily archers. The thing all humans have in common is that they need a name, so the Human class has taken care of the naming logic.

Now we need to write an Archer class. Archers are humans, and therefore need a name, but we don't want to re-write all that code! Let's just inherit the Human class!

Complete the Archer class. It should inherit from its parent. In its constructor it should call its parent's constructor, then also set its unique __num_arrows property.


'''

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
'''
When should I use inheritance?
Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance probably is not the best answer. In that case, you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from.

All cats are animals but not all animals are cats
'''  

'''
Inheritance Hierarchy
There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit from an Animal that inherits from LivingThing. That said, we should always be careful that each time we inherit from a base class the child is a strict subset of the parent. You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

Assignment
The game designers have decided to add a new unit to the game: Crossbowman. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they have an additional method: triple_shot().

Add a use_arrows(self, num) method to the Archer class. It should remove num arrows. If there aren't enough arrows to remove, it should raise a not enough arrows exception.
The Crossbowman classes constructor should call its parent's constructor.
The crossbowman's triple_shot method should use 3 arrows.
The crossbowman's triple_shot method takes a target as a parameter and prints {} was shot by 3 crossbow bolts where {} is the name of the Human that was shot.
'''
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows < num:
            raise Exception("Not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        print(f"{target} was shot by 3 crossbow bolts")
        


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    try:
        print("creating an archer named Bard")
        human2 = Archer("Bard", 1)
        identify(human2)
        print(f"Bard has {human2.get_num_arrows()} arrows")

        print("creating a crossbowman named Sir Not-Appearing-In-This-Film")
        human3 = Crossbowman("Sir Not-Appearing-In-This-Film", 4)
        identify(human3)
        print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
        print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
        human3.triple_shot(human2)
        print(f"{human3.get_name()} has {human3.get_num_arrows()} arrows")
        print(f"{human3.get_name()} attempts to shoot {human2.get_name()}")
        human3.triple_shot(human2)

    except Exception as e:
        print(e)


def identify(human):
    print(f"Getting name: {human.get_name()}")


main()

'''
Inheritance hierarchy quiz
There is no limit to how deeply we can nest an inheritance tree. 
For example, a Cat can inherit from an Animal which inherits from Living_Thing. 
That said, we should always be careful that each time we inherit from a base class that the child is a strict subset of the parent. You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.
'''

'''
Multiple children
So far we've worked with linear class inheritance. In reality, inheritance structures often form trees, not lines. A class can have as many direct child classes as the programmer wants.

Assignment
The Hero class is provided for you. In this assignment you'll be writing the Archer class that inherits from Hero, and in the next assignment you'll be writing its sibling Wizard class.

Fulfill the following requirements from the game designers.

Archer should inherit from Hero
Archer should setup the hero's name and health
Set a private "number of arrows" that can be passed in as a third parameter to the constructor.
Create a shoot method that takes a target human as input. If there are no arrows left, raise a not enough arrows exception. Otherwise, remove an arrow and deal 10 damage to the target human.
'''

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# Create Archer class here
class Archer(Hero):
    def __init__(self, name, health, num_of_arrows):
        super().__init__(name, health)
        self.__num_of_arrows = num_of_arrows

    def shoot(self, target):
        if self.__num_of_arrows <= 0:
            raise Exception("not enough arrows")
        else:
            self.__num_of_arrows -= 1
            target.take_damage(10)


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    try:
        print("Creating a hero named Hercules with 200 health")
        human1 = Hero("Hercules", 200)
        identify(human1)

        print("creating an Archer named Pericles with 100 health and 2 arrows")
        human2 = Archer("Pericles", 100, 2)
        identify(human2)

        while human1.get_health() > 0 and human2.get_health() > 0:
            print(f"{human2.get_name()} attempts to shoot {human1.get_name()}")
            human2.shoot(human1)
            identify(human1)
            identify(human2)

    except Exception as e:
        print(e)


def identify(human):
    print(f"Name: {human.get_name()}, health: {human.get_health()}")


main()

'''
Multiple children
Assignment
Let's extend the Hero class by adding a second child class: the Wizard. Wizard heroes are more powerful than archer heroes. They cast spells at other humans instead of shooting them, and casting does 25 damage instead of 10 but also costs 25 mana.

Fulfill the following requirements.

Wizard should inherit from Hero
Wizard should set up the hero's name and health
Set a private "mana" variable that can be passed in as a third parameter to the constructor.
Create a cast method that takes a target human as input. If there is not enough mana left, raise a not enough mana exception. Otherwise, remove 25 mana from the wizard and deal 25 damage to the target human.
'''
class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


# Create the Wizard class here
class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana
    def cast(self, target):
        if self.__mana <= 0:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
    


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    health = 100
    mana = 400
    print(f"Creating a Wizard named Harry with {health} health and {mana} mana")
    human1 = Wizard("Harry", health, mana)
    identify(human1)

    health = 100
    arrows = 2
    print(f"Creating an Archer named Pericles with {health} health and {arrows} arrows")
    human2 = Archer("Pericles", health, arrows)
    identify(human2)

    while human1.get_health() > 0 and human2.get_health() > 0:
        try:
            print(f"{human2.get_name()} attempts to shoot {human1.get_name()}")
            human2.shoot(human1)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)

        try:
            print(f"{human1.get_name()} attempts to cast at {human2.get_name()}")

            human1.cast(human2)
            identify(human1)
            identify(human2)
        except Exception as e:
            print(e)


def identify(human):
    print(f"Name: {human.get_name()}, health: {human.get_health()}")


main()
'''
Multiple children quiz
You'll often find in production software that it's more likely that an inheritance tree is wide than deep. In other words, instead of a deep tree like:

Organism -> Animal -> Mammal -> Feline -> Cat
You will more often see a wide tree:

Dragon -> Drake
       -> Wyvern
       -> Hydra
       -> Druk
Why are inheritance trees often wide instead of deep?
As we talked about earlier, in good software a child class is a strict subset of its parent class. In a deep tree, that means the children need to be perfect members of all the parent class "types". That simply doesn't happen very often in the real world. It's much more likely that you'll have a base class that simply has many sibling classes that are slightly different variations of the base.

Vehicle -> Truck
        -> Car
        -> Boat
        -> Train
'''