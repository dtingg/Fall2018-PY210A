Mailroom - Object Oriented
===================

OO mailroom is the final project for the class.

So this is your chance to really do things "right". Strive to make this code as good, by every definition, as you can.

With that in mind:

Functionality
-------------

* The logic is correct -- i.e. the program works :-)

* The logic is robust -- you are handling obvious expected errors reasonably:

  - User inputting a non-number as a donation

  - Trying to make a negative donation

  - User getting capitalization or spacing or ??? wrong with a name.

    - Maybe add logic where you tell them that the name is not in the DB, and do they want to create it, rather than simply creating a new record for a typo in a donor name.

Code structure

* Classes should have clear purpose and encapsulation: only the code within a class should know exactly how the data are stored, for instance.

* Anything that only needs to know about one donor should be in the ``Donor`` class

* Anything that needs to know about the collection should be in a ``DonorCollection`` class.

* Any user interaction should be outside the "logic" code. (Sometimes called the "Model", or "Business logic")

  - You should be able to re-use all the logic code with a different UI -- Web App, GUI, etc.

  - There should be no ``input()`` or ``print`` functions in the logic code.

  - The logic code should be 100% testable (without mocking input() or any fancy stuff like that)

Testing

* All logic code should be tested.

* Tests should be isolated to test one thing each

* Tests should (reasonably) check for handling of weird input.

* Tests should be isolated -- that is, they will work if run by themselves, and in any order.

  - This means they should not rely on any global state.

  - you'll probably find this easier with a well structured OO approach -- that is, you can test an individual donor functionality without knowing about the rest of the donors.


The "soft" stuff:

Style:
    - conform to PEP8! (or another consistent style)

    - You can use 95 or some other reasonable number for line length

Docstrings:
    Functions and classes should all have good docstrings. They can be very short if the function does something simple.

Naming:
    All classes, functions, methods, attributes, variables should have appropriate names: meaningful, but not too detailed.

Extra Ideas:
------------

In case you are bored -- what features can you add?

* How about an html report using your html_render code?

* Fancier reporting

* The sky's the limit
