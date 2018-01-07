The technology
==============

Introduction
------------

*AnPyLar* is a Python framework for the web and it achieves this feat by
piggybacking on `*Brython* <https://brython.info>`_ and distributing it
packaged inside ``anpylar.js``

*Brython* is an incredible project and an awesome achievement. And *AnPyLar*
has contributed patches to the upstream to improve it, like for example
improved ``metaclass`` support.

During the development of *AnPyLar* the auto-loadable packages for *Brython*
were also invented.

But *Brython* is also a dynamic and changing environment and this has its
drawbacks:

  - Pointing simply to the latest version of *Brython* could mean that
    *AnPyLar* applications would break.

That's the reason for packaging a well-known (and possibly patched) version
inside ``anpylar.js``.

Some things to take into account
--------------------------------

Being incredible and awesome doesn't imply it is a **complete** and 100%
CPython compatible implementation. It is by far complete enough to create very
complex applications (*AnPyLar* being a good example of it) but this does come
with some price tags, that you as developer have to take into account.

Let's see them and avoid surprises later

  - It's not a complete Python 3.x implementation and even the implemented
    areas may have some quirks. Don't let this put down your idea to use this
    incredible technology, because it can do almost everything *Python 3.x* can
    do

  - It's slower than *Javascript*. This should come to no surprise, because
    it's written (and your scripts transpiled to) in *Javascript*. And yes,
    *Python* itself is slower than *Javascript* to start with due to its
    incredible dynamism and introspection possibilities.

  - Error reporting on the developer console can be difficult to process and
    understand. It just takes time. There are two things to do here

    - Modify little things and test. This will allow you to track only a small
      amount of changes to track to find the error

    - Use ``anpylar-syntaxcheck`` (abbreviate it to ``anpylar-syntax`` if you
      want) and give it a list of files/directories to check the syntax of your
      scripts before running them (or after having seen an error). It uses the
      built-in Python *Abstract-Syntax-Tree* facilities to find syntax errors
      in your code.


On the positive side
--------------------

You are developing in *Python* in the browser and you can create incredible
applications (complex or not)

Just do it!
