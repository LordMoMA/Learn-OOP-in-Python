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

'''
Get edges
Remember that with normal "units" we were checking if their (x/y) point was within a rectangle (the Dragon's breath) to see if they were hit by the fire. With a dragon, because they're so big, we're going to check if the dragon's body (a rectangle) is within the fire (also a rectangle still). The image below contains an example of fire breath hitting a dragon.

overlap

Assignment
In the next assignment, we'll be writing the overlap method itself. First, let's set up some helper methods.

Write the following methods, what they do should be self-explanatory given their names.

get_left_x()
get_right_x()
get_top_y()
get_bottom_y()
Remember that x1 OR x2 could be the "left x" based on its value on the Cartesian plane. The same goes for the y values.
'''

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def describe(rectangle):
    print(
        f"left x: {rectangle.get_left_x()}, right x: {rectangle.get_right_x()}, top y: {rectangle.get_top_y()}, bottom y: {rectangle.get_bottom_y()}"
    )


def main():
    describe(Rectangle(0, 0, 4, 4))
    describe(Rectangle(4, 4, 0, 0))


main()