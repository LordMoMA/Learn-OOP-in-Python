'''
What is polymorphism?
While inheritance is the most unique trait that object-oriented languages claim to have, polymorphism is probably the most powerful.

Polymorphism is the ability of a variable, function or object to take on multiple forms. For example, in a programming language that supports inheritance, classes in the same hierarchical tree may have methods with the same name but different behaviors.

Shapes
Let's look at a simple example.

class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims
In this example the child classes, Dragon and Kraken are overriding the behavior of their parent class's move() method.

Assignment
Dragons are big. As it turns out, they're a lot bigger than most other units in Age of Dragons. Let's override the Dragon's in_area() method to account for that.

First, we'll need a new class that represents a rectangle. Take a look at the main function to see how it's expected to behave. Variables should be passed into the constructor in this order:

x1
y1
x2
y2
'''
class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def describe(rectangle):
    print(
        f"corner1: ({rectangle.x1},{rectangle.y1}) corner2: ({rectangle.x2},{rectangle.y2})"
    )


def main():
    describe(Rectangle(0, 0, 4, 4))
    describe(Rectangle(4, 4, 0, 0))
    describe(Rectangle(2, -2, 3, 4))


main()