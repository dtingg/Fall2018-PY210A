import math
import sys

# don_db = DonorCollection(test_data())

def test_data():
    """ Data to be used as samples for coding and testing."""
    return {"David Andrews" : [200.50, 400.00, 250.75],
            "John Goodfellow" : [25.00, 175.50],
            "Mary Suzuki" : [75.00, 125.00, 250.00],
            "Bonney Lake" : [500.50, 700.75, 500.25],
            "DeMarcus Rollins" : [155.00, 165.00]
            }


class Donor:
    def __init__(self, name, donation=None):
        """ Create Donor class for data and methods for individual donor."""
        self.name = name.strip()
        if donation is None:
            self.donations = []
        else:
            self.donations = list(donations)

    @staticmethod
    def valid_donation(donation):
        """ Make sure entered amount of a donation is valid before adding to database."""
        if donation < 0:
            raise ValueError("Donation has to be more than 0.")
        if donation < 0.1:
            raise ValueError("Donation has to be more than 10 cents")
        return donation

    def add_donation(self, amount):
        amount = self.valid_donation(amount)
        self.donations.append(amount)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def tot_donations(self):
        return sum(self.donations)

    @property
    def avg_donation(self):
        """ Average donation is total donations divided by the number of donations."""
        return self.tot_donations / self.num_donations

    @property
    def last_donation(self):
        try:
            return self.donation[-1]
        except IndexError:
            return None

    def thank_you_letter():
        print("Dear {}, \n"
            "Thank you for your generous gift of ${} to promote public education \n"
            "and to support research about bats. \n"
            "The Bat Society".format(self.name, self.last_donation))


class DonorCollection:
    def __init__(self, donors=None):
        """ Initialize the DonorCollection class to hold info, data, and methods for all donors in database."""
        if donors is None:
            self.donor_inf = {}
        else:
            self.donor_inf = {name: donations}

    @property
    def donors(self):
        return self.donors_inf.keys()

    @property
    def list_of_donors(self):
        dlist = []
        return self.donors.keys()

    @classmethod
    def add_donor(self, donor=None):
        if donor is None:
            donor = {}
        if donor not in don_db:
            don_db.append(donor)

    @classmethod
    def find_donor(self, name):
        if donor in don_db:
            return self.donor
        else:
            print("Donor name not found. Would you like to join?")
            self.add_donor()

    @property
    def thank_all_donors(self, donors):
        return self.thank_all_donors(donors)



def cli_main_menu():
    while True:
        try:
            print("Welcome to the Bat Society. Please select from 1 to 4 in the following: ")
            answer = int(input("1 Send a Thank You letter \n"
                               "2 Create a Report \n"
                               "3 Send letters to all donors \n"
                               "4 Quit \n"))
            if answer == 4:
                print("Thank you for visiting our website.")
                sys.exit()
            elif answer == 1:
                thank_you_letter()
            elif answer == 2:
                make_report()
            elif answer == 3:
                letters_to_donors()
                break
            else:
                print("Please try again choosing from 1 to 4.")
        except ValueError:
            print("Please enter a valid response.")


def thank_you_letter():
    while True:
        name = input("What is your full name? \n"
                    "Type 'list' for a list of donors. \n"
                    "Or type 'menu' to exit. \n"
                    )
        name = name.strip().title()
        if name == "Menu":
            return
        elif name == "List":
            print(don_db.keys())
            choose_name_from_list()
        else:
            print("Welcome back {}.".format(name))
            break
        """ When name not in don_db, add name to database."""
        if name is None:
            donor = don_db.add_donor(name)
    make_donation()
    return

def choose_name_from_list():
    try:
        name = input("Please type in a name from the list: \n")
    except ValueError:
        print("Please type in a valid name.")
    return

def make_report():
    # I have to admit that I couldn't figure out the formatting by myself!
    # Summary report.
    # Show total donation, the number of donations, and the average amount per donation.
    # Print out the results in a table.
    report_rows = []
    for key, value in don_db:
        name = key
        tot_don = sum(value)
        num_don = len(value)
        avg_don = tot_don / num_don
        report_rows.append(name, tot_don, num_don, avg_don)
    report = []
    report.append("{:<25}|{:>16}|{:>16}|{:>16}".format("Donor Name","Total Donation",
                                                 "Num Donations","Average Amount"))
    for row in report_rows:
        report.append("{:<25} {:>16.2f} {:>16d} {:>16.2f}".format(*row))
    return "\n".join(report)


def make_donation():
    # Prompt user to make a donation
    while True:
        don_resp = input("How much would you like to donate? \n"
                     "Or type 'menu' to exit. \n").strip()
        if don_resp in ("menu", "Menu"):
            return
        else:
            try:
                don_resp = float(don_resp)
                break
            except ValueError:
                print("Please enter a valid amount.")
    test_data.update(name[don_resp])
    thank_you_letter()
    return


def letters_to_donors():
    pass



if __name__ == '__main__':
    cli_main_menu()
    make_report()
    thank_you_letter()
    make_donation()
    choose_name_from_list()
    # add_donor()
    # letters_to_donors()






"""
Goal: Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

Mailroom Part 1

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a single module, a simple data structure,
d functions that manipulate that data structure. In fact, you’ve already done that :-)

But if one were to expand the program with additional functionality, it would start to get a bit unwieldy
and hard to maintain. So it’s a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidelines for good code structure:

Encapsulation: You have a data structure that holds your data, and functions that manipulate that data; you
want data and methods “bundled up” in a neat package so that everyting that works with that data structure
are within one unit. The rest of the code doesn’t need to know about the data structure you are using.

Separation of Concerns: The user-interaction code should be cleanly separated from the data handling code.

https://en.wikipedia.org/wiki/Separation_of_concerns

There should be no input functions in the classes that hold the data!

As always: DRY (Don’t Repeat Yourself): Anywhere you see repeated code; refactor it!

The Program
See: Mailroom Part 1 to remind yourself what the program needs to do.

Suggestions
 One of the hardest parts of OO design (particularly in Python) is to know how “low” to go with the classes
and data structures. In particular, you might have a bit of data collected together (say, a donor’s name and
donation history). This can be a simple tuple with a few items in it; a dict with those same data available
as key:value pairs; or a class, with class attributes (and, possibly, methods).

There are no hard and fast rules, but here are some guidelines:

For this assignment it’s OK to go with simple tuples. However, in order for the code to be more flexible in
the future, for example, if new “fields” were added to the donor object, it’s probably better to use a more
structured data type, so you don’t have to worry about changing the order or number of fields.

So now you have to think about using a dict or class. Again for flexibility, I think a dict is a bit easier;
you can add fields to it very easily. However, with a class, you can build some functionality in there, too.
This is where encapsulation comes in. For instance, one thing you might want to do is get the total of all
donations a donor has made in the past. If you add a method to compute that (or a property!), then the rest
of the code doesn’t need to know how the donations are stored.

Consider data[0] vs data["first_name"] vs data.first_name. Which one is more readable? Keep in mind that
another benefit of using OO for data encapsulation is ability of modern IDE to provide auto-completion, which
reduces number of bugs and helps to produce code faster.

Below are more detailed suggestions on breaking down your existing code into multiple modules that will be
part of a single mailroom program.

Modules vs. Classes
You may organize your code to your preference and keep it simple by having all of the code in a single file.

Optionally, you could organize your code into modules, which helps to keep code organized and re-usable.

What is a module? A module is a python file that can be imported in other files. Modules can contain functions,
classes, and even variables (constants).

Here is an example file structure for mailroom_oo package that contains 3 modules:

└── mailroom_oo
   ├── __init__.py
   ├── cli_main.py
   ├── donor_models.py
   └── test_mailroom_oo.py
The module donor_models.py can contain the Donor and DonorCollection classes.

The module cli_main.py would include all of your user interaction functions and main program flow.

Note that __init__.py is an empty file that tells Python that this directory should be treated as a package
so that you can import modules.

Donor Class
Class responsible for donor data encapsulation

This class will hold all the information about a single donor, and have attributes, properties, and methods
to provide access to the donor-specific information that is needed. Remember, if you are writing code that
only accesses information about a single donor, then it should most likely live in this class.

DonorCollection Class
Class responsible for donor collection data encapsulation

This class will hold all of the donor objects, as well as methods to add a new donor, search for a given donor,
etc. If you want a way to save and re-load your data, this class would hold that method, too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.

Command Line Interface
Module responsible for main program flow (CLI - Command Line Interface)

Let’s call this module cli_main.py to represent the entry point for the mailroom program. This module will
be using the classes we defined: Donor and DonorCollection. It will also handle interaction with the user
via the input function calls that gather user input and to provide the output to the console.

What should go into this module?

main “switch dictionary” to map user selection to the program features; in general, you will have a method
for each of the mailroom functions.
input function calls to gather user input
print statements to print to console
Note

Technically, console print statements don’t belong in your data classes. However, for some features of this
program, such as “send letters,” we are simply printing instead of “sending,” so it is ok for this feature
to reside in the data class. But do keep integration of console print statements with data classes to a
minimum. Ideally, the data class methods return a string, and the UI code does the printing.

Why is this separation of data and method so important?

The idea here is that we should be able to fairly easy replace this CLI program with a different type of
interface, such as a GUI (Graphical User Interface), without having to make any changes to our data classes.
If that was the case, then you would implement the GUI elements and use your data classes the same way as
they are used in CLI.

Test-Driven Development
At this point we have done a great job refactoring the more complex code out of data-holding classes and we
are left with simple classes that are more straightforward to unit test. As you build your classes, update
the tests you already have to the logic code to the new API. Ideally, update the tests first, then the code.

The Donor and DonorCollection classes should now have close to 100 percent code coverage.

For the moment, don’t worry about testing most of the command line interface code. That requires simulating
user input, which is an advanced testing topic. But you can (hopefully) see some of the benefits of separating
the user-interaction code from the logic code; your logic code is much easier to test with no user-interaction
involved.

Exercise Guidelines
OO mailroom is the final project for the class.

So this is your chance to really do things “right”. Strive to make this code as good, by every definition,
as you can.

With that in mind:

Functionality
The logic is correct – i.e. the program works :-)
The logic is robust – you are handling obvious expected errors reasonably:
User inputting a non-number as a donation
Trying to make a negative donation
User getting capitalization or spacing or ??? wrong with a name.
maybe add logic where you tell them that the name is not in the DB, and do they want to create it, rather
than simply creating a new record for a typo in a donor name.
Code structure:
Classes should have clear purpose and encapsulation: only the code within a class should know exactly how
the data are stored, for instance.
Anything that only needs to know about one donor should be in the Donor class
Anything that needs to know about the collection should be in a DonorCollection class.
Any user interaction should be outside the “logic” code. (Sometimes called the “Model”, or “Business logic”)
You should be able to re-use all the logic code with a different UI – Web App, GUI, etc.
There should be no input() or print functions in the logic code.
The logic code should be 100% testable (without mocking input() or any fancy stuff like that)
Testing:

All logic code should be tested.
Tests should be isolated to test one thing each
Tests should (reasonably) check for handling of weird input.
Tests should be isolated – that is, they will work if run by themselves, and in any order.
This means they should not rely on any global state.
you’ll probably find this easier with a well structured OO approach – that is, you can test an individual
donor functionality without knowing about the rest of the donors.
Now the “soft” stuff:
Style: conform to PEP8! (or another consistent style)
You can use 95 or some other reasonable number for line length
docstrings: functions and classes should all have good docstrings. They can very very short if the function
does something simple.
Naming: all classes, functions, methods, attributes, variables should have appropriate names: meaningful,
but not too detailed.
Extra ideas:
In case, you are bored – what features can you add?

How about an html report using your html_render code?
Fancier reporting
The sky’s the limit
"""