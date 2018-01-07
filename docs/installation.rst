Installation and Setup
######################

Installation
============

Being this all about Python, it is practical to have a command line manager
that can help in setting up, prototyping, resetting, packaging and doing some
other tasks.

As it is canonical for Python applications, you can install the command line
manager with::

  pip install anpylar

which gives you access to a set commands like for example::

  anpylar-serve <directory-to-serve>

This starts the *AnPyLar* web development server which allows you to test your
application whilst developing.

You can actually invoke the same command as ``anpylar serve`` (notice
there is no ``-`` in between), but we prefer the former because it works
perfectly with shell completion.

.. note:: Under *Unix*-like operating systems, the scripts will be already in
   your path with a default Python installation. Under *Windows* your mileage
   may vary. Most distributions will ask you during installation if you want to
   have them in your *PATH*.

Of course, you may also choose to completely skip the command line application.

Setup
=====

If you use the command line client you can simply do
::

  anpylar-application myapp

This will create a directory named ``myapp`` which will contain an
``index.html`` file like this

.. code-block:: html

   <!DOCTYPE html>
   <html>
   <head>
     <title></title>

     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">

     <link rel="stylesheet" href="styles.css">
     <script src="anpylar.js" async></script>

   </head>
   <body></body>
   </html>

Of course, the reference files ``styles.css`` and ``anpylar.js`` have also been
deployed to the application directory.

For further info we recommend that you go to the **Tutorial: Tour of
Pyroes**. It starts from scratch and shows the layout produced by the different
tools.

Manual Setup
------------

Be it because you don't want to use the command line client or because you
prefer to execute some steps manually, there is only 1 requirement to run your
application: having the ``anpylar.js`` file loaded by your web page.

All that you need then is something like

.. code-block:: html

     <script src="path_to/anpylar.js" async></script>

In this case you will have downloaded the file manually.

or

.. code-block:: html

     <script src="http://example.com/anpylar.js" async></script>

True, you won't be getting it from *example.com*, because the actual canonical
links are:

  - Version specific:
    ``https://cdn.rawgit.com/anpylar/anpylar/VERSION/anpylar.js``

    Just replace ``VERSION`` with your version of choice, for example:
    ``1.1.1``

The aforementioned version contain no line number information. If you want to
preserve that, use the ``_debug`` alternative:

  - Version specific:
    ``https://cdn.rawgit.com/anpylar/anpylar/VERSION/anpylar_debug.js``

    Just replace ``VERSION`` with your version of choice, for example:
    ``1.1.1``
