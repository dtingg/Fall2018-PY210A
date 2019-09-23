######################
HTML Renderer Exercise
######################

Ever need to write some HTML? Maybe from data?

And not want to write all those tags yourself?

OK, maybe not -- but trust me, it's a pain -- let's write some code to do it for us.

HTML Renderer
=============

Goal:
-----

The goal is to create a set of classes to render html pages -- in a "pretty printed" way.

i.e. nicely indented and human readable.

We'll try to get to all the features required to render this file:

https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/sample_html.html

Take a look at it by opening it in your text editor. And also in a browser to see how it's rendered.

If you don't know html -- just look at the example and copy that. And you can read the: `html_primer` at the end of this page for enough to do this exercise. And anyone working with computers these days would benefit from at least a passing familiarity with html.

The exercise is broken down into a number of steps -- each requiring a few more OO concepts in Python.

The goal of the code is to render html. The goal of the *exercise* is to build up a simple object hierarchy with:

* classes
* class attributes
* instance attributes
* methods
* subclassing
* overriding attributes and methods


General Instructions:
---------------------

You can start with the framework in:

https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/html_render.py

For each step, add the required functionality. There is example code to run your code for each step in:

https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/run_html_render.py

You should be able to run that code at each step, uncommenting each new step in ``run_html_render.py`` as you go.

It builds up an html tree, and then calls the ``render()`` method of your element to render the page.

It uses a ``StringIO`` object (like a file, but in memory) to render to memory, then dumps it to the console, and writes a file. Take a look at the render_page function at the top of the file to make sure you understand it.

The html generated at each step will be written to the files named:
``test_html_ouput?.html``

Unit tests
----------

Running the ``run_html_render.py`` script is a (simple) form of integration testing -- it checks how the individual components are working together. But we also want to make sure each individual *unit* (class, method) of code works. So to do that, we'll use:

**Test Driven Development**

In addition to checking if the output is what you expect with the running script -- you should also write unit tests as you go.

Each new line of code should have a test that will run it -- *before* you write that code.

That is:

  1. write a test that exercises the next step in your process
  2. run the tests -- the new test will fail
  3. write your code...
  4. run the tests. If it still fails, go back to step 3...

A start of a test file is provided here:

https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/test_html_render.py

It has a few tests for the first few steps -- uncomment them as you go along.

But it is NOT comprehensive -- you will need to add more tests at every step!

You can run ``pytest`` on that test file first thing -- it should pass two tests (that you can create an Element object -- not that it works) and fail one -- one that actually starts to test functionality.

**NOTE** if you are lost, take a look at the tutorial here:
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer_tutorial.html#html-renderer-tutorial. But do try to do it yourself first.
