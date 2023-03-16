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
            return (
                self.get_left_x() <= rect.get_right_x()
                and self.get_right_x() >= rect.get_left_x()
                and self.get_top_y() >= rect.get_bottom_y()
                and self.get_bottom_y() <= rect.get_top_y()
            )
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
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(
        pos_x - (width / 2),
        pos_y - (height / 2),
        pos_x + (width / 2),
        pos_y + (height / 2),
        )


    def in_area(self, x_1, y_1, x_2, y_2):
        rect = Rectangle(x_1, y_1, x_2, y_2)
        return self.__hit_box.overlaps(rect)
        
        

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.fire_range,
                y - self.fire_range,
                x + self.fire_range,
                y + self.fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

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


def describe(dragon):
    print(
        f"{dragon.name} is at position ({dragon.pos_x},{dragon.pos_y}). height: {dragon.height}. width: {dragon.width}. fire range: {dragon.fire_range}"
    )


def main():
    dragons = [
        Dragon("Green Dragon", -1, -2, 1, 2, 1),
        Dragon("Red Dragon", 2, 2, 2, 2, 2),
        Dragon("Blue Dragon", 4, -3, 2, 1, 1),
        Dragon("Black Dragon", 5, -1, 3, 2, 2),
    ]

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        describe(dragon)

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(i, i, other_dragons)


main()