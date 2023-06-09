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
'''
Dragons
In "Age of Dragons", there are Orcs, Humans, Goblins, Dragons, etc. All of those different creatures are called "units". At the moment, the only thing specific to a unit is that it has a position on the game map and a name.

Dragons, a specific type of unit, can breathe fire in a large area dealing damage to any units that are touched by its fiery blaze.

The game grid
Our game map is just a Cartesian plane.

cartesian

Assignment
Complete the unit's in_area method and the dragon's breathe_fire method.

in_area
If the unit's position is in the rectangle defined by the parameters, return True. Otherwise, return False. x_1 and y_1 make up the bottom-left point of the rectangle. x_2 and y_2 define the top-right point.

breathe_fire
This method causes the dragon to breathe a swath of fire in the target area. The target area is centered at (x,y). The area stretches for __fire_range in either direction inclusively.

For each unit in the units array, print {} is hit by the fire if the unit is within the blast, where {} is the name of the unit.

Example of fire breath hitting a unit
breath hitting unit
'''

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        x1 = x - self.__fire_range
        x2 = x + self.__fire_range
        y1 = y - self.__fire_range
        y2 = y + self.__fire_range
        for unit in units:
            if unit.in_area(x1, y1, x2, y2):
                print(f"{unit.name} is hit by the fire")
    # solution 2
    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")   


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print("Creating an army of generic units")
    units = [
        Unit("Yvor", 1, 0),
        Unit("Nicholas", 0, 1),
        Unit("Eoin", 2, 0),
        Unit("Cian", 3, 3),
        Unit("Andrew", -1, 4),
        Unit("Baran", -6, 5),
        Unit("Carbry", 2, 1),
    ]
    for unit in units:
        print(f"creating {unit.name} at position {unit.pos_x} {unit.pos_y}")

    smaug = Dragon("Smaug", 6, 6, 2)
    print(f"{smaug.name} breathes fire at position 1,1")
    smaug.breathe_fire(1, 1, units)


main()

'''


Dragons
We have written a lot of classes so far, but we haven't written much code that uses the classes and calls their methods.

The code in the test suite is largely the same code that you built in the last assignment. One key difference is the addition of a describe function that you'll be using.

Assignment
Let's use the Dragon class we made to have a little dragon fight. Complete the bottom half of the main() function.

First, describe() each dragon in the dragon array that has been created for you
Next, have each dragon breathe fire at all the other dragons. The center of each blast should always be at (3,3).
Ordering matters for your solution
Make sure to do everything in ascending index order. For example, when Blue Dragon breathes fire, it should breathe fire on the other dragons in this order:

Green Dragon
Red Dragon
Black Dragon
'''
def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # -- TEST SUITE, DONT TOUCH ABOVE THIS LINE --

    for dragon in dragons:
        describe(dragon)
    # have each dragon breathe fire at all the other dragons
    for i in range(len(dragons)):
        for j in range(len(dragons)):
            if i != j:
                dragons[i].breathe_fire(3, 3, [dragons[j]])
'''

Green Dragon is at 0/0

Red Dragon is at 2/2

Blue Dragon is at 4/3

Black Dragon is at 5/-1

Green Dragon breathes fire at 3/3 with range 1

Red Dragon is hit by the fire

Green Dragon breathes fire at 3/3 with range 1

Blue Dragon is hit by the fire

Green Dragon breathes fire at 3/3 with range 1

Red Dragon breathes fire at 3/3 with range 2

Red Dragon breathes fire at 3/3 with range 2

Blue Dragon is hit by the fire

Red Dragon breathes fire at 3/3 with range 2

Blue Dragon breathes fire at 3/3 with range 3

Green Dragon is hit by the fire

Blue Dragon breathes fire at 3/3 with range 3

Red Dragon is hit by the fire

Blue Dragon breathes fire at 3/3 with range 3

Black Dragon breathes fire at 3/3 with range 4

Green Dragon is hit by the fire

Black Dragon breathes fire at 3/3 with range 4

Red Dragon is hit by the fire

Black Dragon breathes fire at 3/3 with range 4

Blue Dragon is hit by the fire
'''

# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()