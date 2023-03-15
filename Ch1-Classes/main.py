'''
What is object-oriented programming?

Object Oriented programming, or "OOP" for short, is a way of writing code that relies on the concepts of classes and objects. The main benefit of writing your code in an object-oriented way is to structure your program into simple, reusable pieces of code.
In this course, we'll be coding the pieces of a real-time strategy game called "Age of Dragons". Players will control armies of men, elves, orcs and dragons as they fight with one another online. If you're familiar with Age of Empires, WarCraft, or StarCraft, it will be something like that.

Assignment
Your manager has noticed that there's a lot of repetitive code in the "Age of Dragons" code base. She has tasked you with reworking the fight_soldiers function so that the DPS (damage-per-second) calculation logic is only written once.

Notice how these two lines are practically identical:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
Finish the get_soldier_dps() function and use it in the fight_soldiers function. get_soldier_dps should take a soldier (which is a dictionary) and return its DPS. It's the same logic that currently exists in fight_soldiers, but now we'll only need to write it in a single place.

def get_soldier_dps(soldier):
    # ?


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
'''
def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print(
        fight_soldiers(
            {"damage": 10, "attacks_per_second": 3},
            {"damage": 20, "attacks_per_second": 1},
        )
    )
    print(
        fight_soldiers(
            {"damage": 50, "attacks_per_second": 1},
            {"damage": 50, "attacks_per_second": 2},
        )
    )
    print(
        fight_soldiers(
            {"damage": 100, "attacks_per_second": 1},
            {"damage": 1, "attacks_per_second": 200},
        )
    )
    print(
        fight_soldiers(
            {"damage": 100, "attacks_per_second": 1},
            {"damage": 50, "attacks_per_second": 2},
        )
    )
    print(get_soldier_dps.__name__)


main()

'''
Clean code
Object-oriented programming and other paradigms like functional programming are all about making code easier to work with and understand. We call code that is easy to work with "clean code".

Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

-- Martin Fowler

Clean code is not
A way to make your programs run faster
A way to make your program use less memory
Necessary to create certain kinds of programs
Strictly better than non-OOP code
Clean code is
Designed to make code easier to work with in many situations
Something that helps humans model the real world
A way to make finding and fixing bugs easier
A way to make new feature development faster
The best way to stay sane as a software engineer

DRY code
Take a look at the code we wrote. We started with this:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
And refactored the code to look like this:

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)
Don't repeat yourself (DRY)
We don't want too much of our code doing the same thing. When code is duplicated, it leads to many potential problems. In our example, let's pretend the soldier dictionary changed, and now the key that stores the "damage" value is called dmg.

In the first example, we would need to update two lines of code. In the second example, we only need to make the change in one place.

It's not a big deal when two lines are the same and exist right next to each other. However, imagine if we had done this several hundred times in ten or twenty different code files! All of sudden, it makes a lot of sense to stop repeating yourself and write more reusable functions. We call that DRY code.
'''

####################################################################

'''
Classes
A class is a special type of value in an object-oriented programming language like Python. Just like a string, integer or float, a class is essentially a custom type that has some special properties.

An object is an instance of a class type. In this example, health is an instance of an integer type.

health = 50
In object-oriented programming, we create special types called "classes". And each instance of a class is called an "object".

How do I create a class?
In Python, you just need to use the class keyword, and you can set custom properties in the following way. It is a common convention in Python to capitalize the first character in name of your class.

class Soldier:
    health = 5
Then to create an instance of a Soldier we simply call the class. Notice that a class isn't a function, it doesn't take input parameters directly.

first_soldier = Soldier()
print(first_soldier.health)
# prints "5"
Assignment
Create a class called Wall on line 1. It should have a property called armor that is initialized to 10 and a height that starts at 5.
'''

class Wall:
    armor = 10
    height = 5

# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    wall = Wall()
    print(wall.armor)
    print(wall.height)


main()

#######################################################

'''
Methods

After the last exercise, you might be wondering why classes are useful, they seem like dictionaries but worse!

What makes classes cool is that they allow us to define custom methods on them. A method is a function that is associated with a class, and it has access to all the properties of the object.

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"
The special "self" value
As you can see, methods are nested within the class declaration. Methods always take a special parameter as their first argument called self. The self variable is a reference to the object itself, so by using it you can read and update the properties of the object.

Notice that methods are called directly on an object using the dot operator.

object.method()
Assignment
Add a fortify() method to your wall class. It should double the current armor property.
'''
class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    wall = Wall()
    print(wall.armor)
    print(wall.height)
    wall.fortify()
    print(wall.armor)
    print(wall.height)
    wall.fortify()
    print(wall.armor)
    print(wall.height)


main()

'''
Methods can return values
If a normal function doesn't return anything, it's typically not a very useful function. Methods often don't return anything explicitly because they often mutate the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values as well!

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"
Assignment
Add a get_cost() method to your wall class. The cost of a wall is a function of the wall's height and armor:

cost = armor * height
'''
class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def fortify(self):
        self.armor *= 2


def main():
    wall = Wall()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")

    print("fortifying wall...")
    wall.fortify()
    print(f"Cost of wall: {wall.get_cost()}")


main()

'''
Methods vs Functions
What is a function?
A function is a piece of code that is called by a name. It can be passed data to operate on via parameters and can optionally return data. All data that is passed to a function is explicitly passed through parameters.

What is a method?
A method is a piece of code that is called by a name that is associated with an object. Methods and functions are similar but have two key differences.

A method is implicitly passed the object on which it was called. In other words, you won't see all the inputs in the parameter list
A method can operate on data that is contained within the class. In other words, you won't see all the outputs in the return statement.
The OOP debate
Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.

For example, while methods are more implicit and often make code more difficult to read, they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase.
'''
##########################################
'''
Constructors (or initializers)
It's quite rare in the real world to see a class that defines properties in the way we've been doing it.

class Soldier:
    armor = 2
    num_weapons = 2
It's much more practical to use a constructor. In Python, the constructor is the init() method, and it is called when a new object is created.

So, with a constructor, the code would look like this.

class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2
However, because the constructor is a method, we can now make the starting armor and number of weapons configurable with some parameters.

class Soldier:
    def __init__(self, armor, num_weapons):
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier(5, 10)
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"
Assignment
Add a constructor to our Wall class. It should take depth, height and width as parameters, and set them as properties. It should also compute an additional property called volume. Volume is the width times height times depth.
'''

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width
    

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    wall = Wall(2, 3, 4)
    print(wall.volume)
    wall = Wall(3, 4, 5)
    print(wall.volume)
    wall = Wall(4, 5, 6)
    print(wall.volume)
    print(wall.height)
    print(wall.width)
    print(wall.depth)


main()

'''
Multiple Objects
If a class is just a type, then an object is just a value.

You'll hear often that an object is an "instance" of a class. Let's look at what that word means.

In object-oriented programming, an instance is a concrete occurrence of any object... "Instance" is synonymous with "object" as they are each a particular value... "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.

-- Wikipedia

So for our wall class, I can create three different "instances" of the class. Or in other words, I'll create three separate objects.

south_wall = Wall(1, 2, 3)
north_wall = Wall(4, 5, 6)
east_wall = Wall(9, 8, 7)

height = 3
width = 4
depth = 5
In the example above, Wall and Integer are types, and each variable is an instance of one of those types.

Assignment
Take a look at the Brawler class and the fight function provided. In the main function, create 4 new brawlers with the following stats:

Name: Aragorn. Speed: 4. Strength: 4.
Name: Gimli. Speed: 2. Strength: 7.
Name: Legolas. Speed: 7. Strength: 7.
Name: Frodo. Speed: 3. Strength: 2.
Then call fight twice. The first fight should be Aragorn vs Gimli. The second will be Legolas vs Frodo.
'''
def main():
    aragorn = Brawler(4, 4, "Aragorn")
    gimli = Brawler(2, 7, "Gimli")
    legolas = Brawler(7, 7, "Legolas")
    frodo = Brawler(3, 2, "Frodo")

    fight(aragorn, gimli)
    fight(legolas, frodo)


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()