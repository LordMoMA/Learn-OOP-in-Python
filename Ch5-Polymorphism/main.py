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

'''
Polymorphism Review
Take a look at the Greek roots of the word "polymorphism".

"poly" means "many".
"morph" means "to change" or "form".
Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).

A classic example is a Shape class that Rectangle, Circle, and Triangle can inherit from. With polymorphism, each of these classes will have different underlying data. The circle needs a center and radius. The rectangle needs two co-ordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

By making each class responsible for its data and its code, you can achieve polymorphism. In this example, each class would have its own Draw() method. This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the same even though they are different. It hides the complexities of the difference behind a clean abstraction.

shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
for shape in shapes:
    print(shape.Draw())
This is in contrast to the functional way of doing things where you would have had separate functions that have different function signatures, like draw_rectangle(x1, y1, x2, y2) and draw_circle(center, radius).

Wait, what is a "function signature"?
A function signature includes the name, inputs, and outputs of a function or method. For example, these two classes have the same method signatures.

class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
Both methods have the same name, take 0 inputs, and return integers. If any of those things are different, they would have different function signatures.

Here is an example of different signatures.

class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
When overriding methods, use the same function signature
If you change the function signature of a parent class when overriding a method, it could be a disaster. The whole point of overriding a method is so that the caller of your code doesn't have to worry about what different things are going on inside the methods of different object types.
'''

'''
Operator Overloading
Another kind of built-in polymorphism in Python is the ability to override an operator in Python depending on the operands used.

Arithmetic operators work for built-in types like integers and strings.

print(3 + 4)
# prints "7"

print("three " + "four")
# prints "three four"
Custom classes on the other hand don't have any built-in support for those operators:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
However, we can add our own support! The __add__ method is used by the Python interpreter when instances of a class are being added with the + operator.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
When you call p1 + p2 under the hood the interpreter just calls p1.__add__(p2).

Assignment
In Age of Dragons, players can upgrade the weaponry of their armies. If a player has two "bronze" swords, they can craft them together to create an "iron" sword. Likewise, two iron swords can be crafted together to create a "steel" sword. If a player tries to craft anything other than 2 bronze swords or 2 iron swords, a can not craft exception is raised.

To make crafting simple for other developers, we'll use operator overloading on the Sword class. The + operator should craft the swords.

type is a string, either bronze, iron or steel.
'''
class Sword:
    def __init__(self, type):
        self.type = type

    def __add__(self, other):
        if self.type == other.type:
            if self.type == 'bronze':
                return Sword('iron')
            elif self.type == 'iron':
                return Sword('steel')
        raise Exception('Can not craft')

'''

creating sword1 that is bronze and sword2 that is bronze

crafting sword1 and sword2 into a new sword3...

sword3 is iron

creating sword4 that is iron

crafting sword3 and sword4 into a new sword5...

sword5 is steel

creating sword6 that is steel

crafting sword5 and sword6 into a new sword7...

Can not craft
'''
# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    try:
        sword1 = Sword("bronze")
        sword2 = Sword("bronze")
        print(f"creating sword1 that is {sword1.type} and sword2 that is {sword2.type}")
        print("crafting sword1 and sword2 into a new sword3...")
        sword3 = sword1 + sword2
        print(f"sword3 is {sword3.type}")
        sword4 = Sword("iron")
        print(f"creating sword4 that is {sword4.type}")
        print("crafting sword3 and sword4 into a new sword5...")
        sword5 = sword3 + sword4
        print(f"sword5 is {sword5.type}")

        sword6 = Sword("steel")
        print(f"creating sword6 that is {sword6.type}")
        print("crafting sword5 and sword6 into a new sword7...")
        sword7 = sword5 + sword6
    except Exception as e:
        print(e)


main()

'''
Operator Overload Review
As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators. Here's a list of how the operators translate into method names.

Operation	Operator	Method
Addition	+	add
Subtraction	-	sub
Multiplication	*	mul
Power	**	pow
Division	/	truediv
Floor Division	//	floordiv
Remainder (modulo)	%	mod
Bitwise Left Shift	<<	lshift
Bitwise Right Shift	>>	rshift
Bitwise AND	&	and
Bitwise OR	|	or
Bitwise XOR	^	xor
Bitwise NOT	~	invert
HelpReport Issue
'''

'''
Overloading Built-in Methods
Last but not least, let's take a look at some of the built-in methods we can overload in Python. While there isn't a default behavior for the arithmetic operators like we just saw, there is a default behavior for printing a class.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# prints "<Point object at 0xa0acf8>"
That's not super useful! Let's teach instances of our Point object to print themselves. The __repr__ method (short for "represent") lets us do just that. It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"
Assignment
Dragons are egotistical creatures, let's give them a great format for announcing their presence in "Age of Dragons". When print() is called on an instance of a Dragon, the string I am {0}, the {1} dragon should be printed.

{0} is the name of the dragon.
{1} is the color of the dragon.
'''
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"I am {self.name}, the {self.color} dragon"


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    print(Dragon("Smaug", "red"))
    print(Dragon("Saphira", "blue"))
    print(Dragon("Nefarian", "black"))
    print(Dragon("Toothless", "blackish"))


main()

'''

I am Smaug, the red dragon

I am Saphira, the blue dragon

I am Nefarian, the black dragon

I am Toothless, the blackish dragon
'''