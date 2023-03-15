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