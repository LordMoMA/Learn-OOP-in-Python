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

'''
Check if rectangles overlap
Assignment
Let's write the overlaps() method, it should return True if the rectangles overlap, and False otherwise. Keep in mind that we want our overlap to be inclusive. If the rectangle's edges are on top of each other, that counts as overlapping.

The logic for two overlapping rectangles, A and B, involves 4 conditions. If all of the following conditions are True then the rectangles overlap:

A's left edge is left of B's right edge
A's right edge is right of B's left edge
A's top edge is above B's bottom edge
A's bottom edge is below B's top edge
'''

class Rectangle:
    def overlaps(self, rect):
        return self.x2 >= rect.x1 and self.x1 <= rect.x2 and self.y1 <= rect.y2 and self.y2 >= rect.y1

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

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


def describe(r):
    print(
        f"left x: {r.get_left_x()}, bottom y: {r.get_bottom_y()}, right x: {r.get_right_x()}, top y: {r.get_top_y()}"
    )


def test(r1, r2):
    print("describing r1")
    describe(r1)
    print("describing r2")
    describe(r2)
    print(f"r1 overlaps r2: {r1.overlaps(r2)}")
    print(f"r2 overlaps r1: {r2.overlaps(r1)}")
    print("========")


def main():
    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(3, 3, 6, 6)
    test(r1, r2)

    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(5, 5, 8, 8)
    test(r1, r2)

    r1 = Rectangle(0, 0, 4, 4)
    r2 = Rectangle(4, 4, 8, 8)
    test(r1, r2)


main()

'''
Bringing it together in the Dragon class
Let's bring all we've done together in the Dragon class. The Dragon class should override the Unit class's in_area method. Instead of checking if the center position of the Dragon is in the given area, we'll check if its big dragon body overlaps with the given area.

Assignment
First, complete the Dragon's constructor. The dragon needs one more private data member: __hit_box. The hitbox is a Rectangle object. You've been provided with the height, width, and center position (pos_x, pos_y) of the dragon.

Example hitbox

in_area() method()
Next, you'll need to override the in_area method. Create a new rectangle object with the given corner positions, and use the rectangle's overlaps method to check if the Dragon is inside it. This method should return a boolean value.
'''