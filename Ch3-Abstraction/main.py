'''
Abstraction
Abstraction is one of the key concepts of object-oriented programming. The goal of abstraction is to handle complexity by hiding unnecessary details. As you can see, abstraction and encapsulation typically go hand in hand, and if we aren't careful with our definitions, they can seem like the same thing.

Abstraction vs encapsulation
While definitions are always changing, I like to think about abstraction and encapsulation in the following way.

Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.
If you want a longer read on the topic, check out this essay.

So are we encapsulating or abstracting our code when we make private data and methods?
Both. Almost always we are doing both. The process of using the double underscore is an encapsulation method. The process of deciding which data deserves to be hidden behind the double underscore is an abstraction. Let's look at a concrete example.

import random

my_random_number = random.randrange(5)
In this example, we're using the random library to generate a random number. As it turns out, generating random numbers is a really hard problem. The operating system actually uses the physical hardware state of the computer as an input to seed the randomness. However, the developers of the random library have abstracted that complexity away and encapsulated a lot of that data and behavior so we don't need to worry about it. We just say "I want a random number less than or equal to 5" and the library takes care of it for us.

The decision to take a single number as input to the randrange function was a decision of abstraction. When writing production-level software, getting the abstractions right is crucial, because they are the hardest things to change later. Think about the consequences of the random package maintainers changing the input parameters to the randrange function! It would break code all over the world.

Assignment
A Human class with a constructor has already been created for you. We don't want the other game developers using our Human class to have to worry about how humans move, we'll abstract that data away from them by encapsulating the private __pos_x, __pos_y, and __speed variables.

Let's add the methods our users will actually call.

move_right(): Adds the human's speed to its x position
move_left(): Subtracts the human's speed from its x position
move_up(): Adds the human's speed to its y position
move_down(): Subtracts the human's speed from its y position
get_position(): Returns the x position and y position as a tuple
'''
class Human:

    def move_right(self):
        self.__pos_x += self.__speed
    def move_left(self):
        self.__pos_x -= self.__speed
    def move_up(self):
        self.__pos_y += self.__speed
    def move_down(self):
        self.__pos_y -= self.__speed
    def get_position(self):
        return (self.__pos_x, self.__pos_y)

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed


def main():
    print("creating a human. x=0 y=0 speed=5")
    human = Human(0, 0, 5)
    print_position(human)

    print("moving left...")
    human.move_left()
    print_position(human)

    print("moving left...")
    human.move_left()
    print_position(human)

    print("moving right...")
    human.move_right()
    print_position(human)

    print("moving up...")
    human.move_up()
    print_position(human)

    print("moving up...")
    human.move_up()
    print_position(human)

    print("moving down...")
    human.move_down()
    print_position(human)


def print_position(human):
    x, y = human.get_position()
    print(f"Your human is at x={x}, y={y}")


main()