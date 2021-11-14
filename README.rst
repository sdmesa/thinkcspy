How to Think Like a Computer Scientist: Interactive Edition
===========================================================

This project began with the original How to Think Like a Computer Scientist text by Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris  Meyers, and Dario Mitchell.  Since 2011 Brad Miller, David Ranum, Barbara Ericson, Mark Guzdial, and many others have built on the text making it interactive.

Programming is not a "spectator sport".  It is something you do,
something you participate in. It would make sense, then,
that the book you use to learn programming should allow you to be active.
That is our goal.

This book is meant to provide you with an interactive experience as you learn
to program in Python.  You can read the text, watch videos,
and write and execute Python code.  In addition to simply executing code,
there is a unique feature called 'codelens' that allows you to control the
flow of execution in order to gain a better understanding of how the program
works.

Getting Started
===============

If you simply want to check it out, read it or whatever,
then you're done.
You can see and read this book `online <https://sdmesa.github.io/thinkcspy>`.

Building this book from source
==============================
We have tried to make it easy for you to build and use this book.  
You can build it and host it yourself in just a few simple steps.

Use whichever of these methods works best for you.

Install Docker and use a docker container
-----------------------------------------
If you don't already have a python development environment setup,
I personally think this is easiest.
Plus I use docker for other things every day.

1. Install `Docker <https://www.docker.com/>`
2. Get the Runestone docker image.

   The `repo <https://github.com/DaveParillo/runestone-docker>`
   has instructions and everything you need to build the image,
   or you can just pull the latest from docker hub:

   :: 

      docker pull dparillo/runestone

For details running and using the container, refer to the
`README <https://github.com/DaveParillo/runestone-docker/blob/master/README.md>`

Install and make a Python virtualenv
------------------------------------
 
* Documentation here:  https://virtualenv.pypa.io/en/stable/
* Video here:  https://www.youtube.com/watch?v=IX-v6yvGYFg
* For the impatient:

::

    $ sudo pip install virtualenv
    $ virtualenv /path/to/some/directory
    $ source /path/to/some/directory/bin/activate

     
* You will need to do the last command **every time** you want to work on the book in your virtual environment.
If you have not used Python virtual environments before I strongly recommend reading the docs or watching the video
 
With the virtual environment installed and configured you can continue.

::

    $ pip install runestone

    $ runestone build -- will build the html and put it in ``./docs/``
    $ runestone serve   -- will start a webserver and serve the pages locally from ``./docs/``


