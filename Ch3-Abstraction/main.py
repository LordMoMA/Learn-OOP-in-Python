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
        return self.__pos_x, self.__pos_y

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

'''
Abstraction vs encapsulation quiz
While definitions are always changing, I like to think about abstraction and encapsulation in the following way.

Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.
For example, using the double underscore convention to hide a __speed variable in Python is an encapsulation technique. In C++ we would use the private keyword to accomplish the same thing. Alternatively, creating a public method called move() that uses the encapsulated __speed variable would be an abstraction.

If you want a longer read on the topic, check out this essay.
https://web.archive.org/web/20210513154547/https://www.tonymarston.net/php-mysql/abstraction.txt
'''

'''
Sprint
Let's add some more abstract features to our Human class! In the game we're making, Age of Dragons, humans can sprint allowing them to move twice as fast. However, sprinting requires stamina. Each time a human sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.

Assignment
Complete all of the missing methods.

The __raise_if_cannot_sprint and __use_sprint_stamina are private methods that are only intended to be used within the class. In your case, you'll use them to build the other four sprinting methods.

__raise_if_cannot_sprint
This method should raise the exception: "not enough stamina to sprint" if the human is out of stamina.

__use_sprint_stamina
Remove one stamina from the human.

The remaining methods
Raise an error if there isn't enough stamina to sprint (use __raise_if_cannot_sprint()).
Use the stamina needed to sprint (use __use_sprint_stamina())
Move twice in the direction of the sprint.
'''
class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_right()
        self.move_right()
    
    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_left()
        self.move_left()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_up()
        self.move_up()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_down()
        self.move_down()

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # -- TEST SUITE, DONT TOUCH BELOW THIS LINE --

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina


def main():
    try:
        print("creating a human. x=0 y=0 speed=5")
        human = Human(0, 0, 5, 3)
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting left...")
        human.sprint_left()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving right...")
        human.move_right()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("moving up...")
        human.move_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting up...")
        human.sprint_up()
        print_position(human)
    except Exception as e:
        print(e)

    try:
        print("sprinting down...")
        human.sprint_down()
        print_position(human)
    except Exception as e:
        print(e)


def print_position(human):
    x, y = human.get_position()
    print(f"Your human is at x={x}, y={y}")


main()

'''
How OOP developers think
As we saw in the last exercise class variables can be private, but methods can be private as well. In other words, we can encapsulate behavior as well as data.

Grouping data and behavior
Classes in object-oriented programming are all about grouping data and behavior together in one place: an object. Object-oriented programmers tend to think about programming as a modeling problem. They think, "how can I write a Human class that simulates the data and behavior of a real human?"

We aren't focusing on functional programming in this course, but to provide some contrast, functional programmers tend to think of their code as inputs and outputs. "When a human acts, what are the inputs to that action, and how do the outputs affect my program state?"

Both paradigms are valuable
While OOP isn't the only paradigm in programming, it's a tried and true one that is useful in a variety of circumstances. In any event, if you have an understanding of multiple ways of thinking about code, you'll be a much better developer overall.
'''
